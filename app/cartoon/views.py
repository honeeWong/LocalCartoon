"""

Description: 用于页面的显示。
Author     : W.Honee
Version    : V0.0.1
Last Change: 2017-07-22

"""
#
# flask的基本功能导入
#
from flask import Flask, render_template, redirect

# 导入蓝图
from . import cartoon

""" 主要页面定义 """

#
# 此处为路由功能，由装饰器实现。
#
@cartoon.route('/')
def index():
    ''' 主页面 '''
    print("显示主页面")
    return render_template("index.html")
