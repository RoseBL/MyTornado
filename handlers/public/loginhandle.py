# coding=utf-8

from handlers.base.basehandle import BaseHandler
from handlers.public.sql_orm import User

class LoginHandle(BaseHandler):
    """
    首页处理类
    """

    def get(self):
        """
        GET请求
        :return:
        """
        self.set_cookie("n1", "v1")
        self.write('Tornado测试应用\n')
        self.write('login\n')
        username = "hq"
        password = "123456"
        user = User()
        user.open()
        # user.add("hq", "123456", "2021-4-1", "lbinxx@163.com", "1024", "normal", "xxx", "12:15")
        if user.compare(username, password):
            print("ok---")
            self.write("OK")

    # def post(self):
    #     """
    #     POST请求,验证用户登录
    #     :return:
    #     """
    #
    #     # 定义响应字典
    #     response = dict()
    #
    #     try:
    #
    #         # 获取用户输入参数
    #         user_name = self.get_argument('userName', default=None, strip=True)
    #         password = self.get_argument('password', default=None, strip=True)
    #
    #         # 业务逻辑简单处理
    #         if user_name == 'admin' and password == '123456':
    #             response['status'] = 200
    #             response['result'] = '登录成功'
    #
    #         else:
    #             response['result'] = '登录失败'
    #
    #     except Exception as exception:
    #
    #         response['status'] = 500
    #         response['msg'] = '服务器奔溃了'
    #         response['exception'] = str(exception)
    #
    #     # 响应处理结果
    #     self.write(response)



