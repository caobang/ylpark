# -*- coding: UTF-8 -*-
import os
import sys
root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, 'venv/Lib/site-packages'))

from flask_script import Manager
from app import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()