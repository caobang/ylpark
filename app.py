# -*- coding: UTF-8 -*-  
import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))
sys.path.insert(1, os.path.join(root, 'Lib/site-packages'))

from flask import Flask
from robot import robot
from werobot.contrib.flask import make_view

app = Flask(__name__)

@app.route('/weixin/',endpoint='werobot',methods=['GET', 'POST'])
def index():
	return make_view(robot)



@app.route('/hello/')
def hello():
	return 'hello1'

if __name__ == '__main__':
	app.run()
