# coding=utf-8

import tornado
import tornado.httpserver  # 异步非阻塞HTTP服务器模块
import tornado.web  # Web框架模块
import tornado.options  # 解析终端参数模块
import tornado.escape  # HTML、JSON、URLs等编码解码和字符串操作
from settings import config
from handlers.urls import urls
import logging

if __name__ == '__main__':
    # 应用配置
    app = tornado.web.Application(urls, **config.settings)

    # 多进程模式
    http_server = tornado.httpserver.HTTPServer(app)

    # 绑定端口
    http_server.bind(config.port)

    # 启动进程数，0表示根据CPU核心数启动进程
    http_server.start(config.process)

    # 配置日志路径
    logging.basicConfig(level=logging.DEBUG, filename=config.log_path)

    # 链接epoll，启动服务
    print('Tornado服务器启动...')
    tornado.ioloop.IOLoop.current().start()
