# -*- coding: UTF-8 -*-
from flask import render_template
from . import route
 
@route.route('/')
def index():
    return render_template('index.html')