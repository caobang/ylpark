# -*- coding: UTF-8 -*-
from flask import Flask

def create_app():
    app = Flask(__name__)

    from . import main,wx
    app.register_blueprint(main.route)
    app.register_blueprint(wx.route, url_prefix='/weixin')

    return app