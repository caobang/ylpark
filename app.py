import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'site-packages'))
sys.path.insert(1, os.path.join(root, 'Lib/site-packages'))

from flask import Flask
from robot import robot
from werobot.contrib.flask import make_view

app = Flask(__name__)
app.debug = True

app.add_url_rule(rule='/weixin/',
                 endpoint='werobot',
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])

@app.route('/hello/')
def hello():
	return 'hello'

if __name__ == '__main__':
	app.run()
