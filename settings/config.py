# coding=utf-8

import os

# 端口
port = 8080

# 开启的进程
process = 1

# app配置
settings = {
    'template_path': os.path.join(os.getcwd(), 'templates'),
    'static_path': os.path.join(os.getcwd(), 'statics'),
    'cookie_secret': '0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies': False,
    'login_url': '/login',
    'debug': True
}

# 运行日志
log_path = os.path.join(os.getcwd(), 'logs/log.txt')
