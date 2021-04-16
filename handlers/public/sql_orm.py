from sqlalchemy import Column, String, create_engine
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.exc import NoResultFound

# 生成orm基类
Base = declarative_base()


class User(Base):
    # 表的名字
    __tablename__ = "user"
    # 表的结构:
    username = Column(String(15), primary_key=True)
    password = Column(String(32))
    time = Column(String(32))
    email = Column(String(128))
    nextReportId = Column(String(255))
    type = Column(String(64))
    description = Column(String(4096))
    lastlogin = Column(String(32))

    session = None
    isClosed = True

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    # 如果User表不存在的话，就创建改表

    def open(self, host="192.168.2.208", port=3306, db="fuzz", user="root", pwd="123456"):
        url = "mysql+pymysql://%s:%s@%s:%d/%s" % (user, pwd, host, port, db)
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        self.isClosed = False
        return self.session

    def add(self, username, password, time, email, nextReportId, type, description, lastlogin):
        new_user = User(username=username, password=password, time=time, email=email,
                        nextReportId=nextReportId, type=type, description=description, lastlogin=lastlogin)
        # 添加到session:
        self.session.add(new_user)
        try:
            # 提交即保存到数据库:
            self.session.commit()
        except IntegrityError as e:
            self.open()
            print(e)
            return "error"
        except:
            return "error"
            # 关闭session:
        self.session.close()

    def delete(self, param, item):
        # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
        user = self.session.query(User).filter(getattr(User, param) == item).delete()
        # 提交即保存到数据库:
        self.session.commit()
        # 关闭Session:
        # self.session.close()

    def query(self, param, item):
        user = self.session.query(User).filter(getattr(User, param) == item).one()
        # print(user.FIRST_NAME)
        try:
            uuu = user.to_json()
            print(uuu)
            return user
        except IntegrityError as e:
            self.open()
            print(e)
            return "error"
        # 关闭Session:
        # self.session.close()

    def update(self, param, value, item, update):
        sss = self.session.query(User).filter(getattr(User, param) == value).update({item: update})
        # 提交即保存到数据库:
        self.session.commit()
        # 下面代码可以使用，但是不推荐下面写法
        # try:
        #     # 提交即保存到数据库:
        #     user = self.session.query(User).filter(getattr(User, param) == value).one()
        #     sss = self.session.query(User).filter(getattr(User, param) == value).update({item:update})
        #     # setattr(user, item, update)
        #     self.session.commit()
        # except NoResultFound as e:
        #     self.open()
        #     print(e)
        #     return "error"
        # except:
        #     return  "error"

    def compare(self, username, password):
        # 查询数据库username的password
        dt_password = self.query("username", username)
        # 将数据库的密码与输入的密码对比
        if password == dt_password.password:
            return True
        else:
            return False
