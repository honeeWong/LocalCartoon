#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Description: 局域网图片网站程序主文件，执行此文件启动网站服务程序。
Author     : W.Honee
Version    : V0.0.1
Last Change: 2017-07-22

"""

""" 导入配置文件 """
import os

def environInit(path="option"):
    '''option文件存有网站的主要配置'''
    load_path = os.path.abspath(os.path.dirname(__file__)) + "/" + path
    if os.path.exists(load_path):
        for line in open(load_path):
            if line[0] != "#":
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0].strip()] = var[1].strip()
    else:
        print("文件不存在！"+load_path)

#
# 必须在所有启动之前调用此函数。
#
environInit()


""" Flask 网站编程 """


#
# app 文件夹 __init__.py 需要定义的对象
#
from app import create_app
#
# flask script 扩展flask app的可操作参数，按照如下格式进行定义:
# def Function():
#     some functions
# 然后加入到command 中，按照如下格式
# manager.add_command('func', Function)
# 一般有如下三种方式实现：
#                       创建Command的子类
#                       使用 @command 修饰符
#                       使用 @option 修饰符
#
from flask_script import Manager, Shell, Server
#
# app create, app 作为承载所有flask动作的入口
#
# application 用于gunicorn启动部署用，而app用于调试
#
application = app = create_app();
#
# manager增加app的启动配置项目,主要方便在服务器端进行各种配置。
#
manager = Manager(app)
#
# debug时使用
#
manager.add_command("runserver", Server(host="0.0.0.0",))


""" 执行 """

if __name__ == '__main__':    
    manager.run()

