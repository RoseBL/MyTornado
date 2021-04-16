# coding=utf-8

from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """
    基本操作类，之后的类可以直接继承
    """

    def set_default_headers(self):
        """
        设置默认的响应头
        :return:
        """

        # 解决JS跨域请求问题
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Content-type', 'application/json')

        # 设置服务器标识，安全考虑
        self.set_header('Server', 'WebServer')
