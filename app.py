import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))
sys.path.insert(1, os.path.join(root, 'Lib/site-packages'))

from robot import robot
from bottle import Bottle
from werobot.contrib.bottle import make_view

app = Bottle()
app.route('/weixin/',
         ['GET', 'POST'],
         make_view(robot))

@app.route('/hello/')
def hello():
	return 'hello'

if __name__ == '__main__':
	app.run()
