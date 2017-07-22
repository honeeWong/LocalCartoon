"""

Description: cartoon文件夹的窗口，此文件夹主要用于显示页面
Author     : W.Honee
Version    : V0.0.1
Last Change: 2017-07-22

"""

#
# 引入蓝图机制，方便后续扩展
#
from flask import Blueprint

cartoon = Blueprint('cartoon', __name__)

from . import views