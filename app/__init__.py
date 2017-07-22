"""

Description: app文件夹包含此程序主要后台及前台内容，所有实现的细节都在这个文件夹，此文件是app文件作为一个对象的窗口。
Author     : W.Honee
Version    : V0.0.1
Last Change: 2017-07-22

"""

# 
from flask import Flask, render_template

from .cartoon import cartoon as cartoon_blueprint




def create_app():
    ''' 初始化创建应用，此处可增加其他初始化动作 '''
    app = Flask(__name__)    
    print("创建app")
    app.register_blueprint(cartoon_blueprint)
    print("导入蓝图")
    return app
