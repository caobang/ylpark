# -*- coding: UTF-8 -*-
import os
import sys

from flask_script import Manager
from app import create_app

app = create_app()
manager = Manager(app)

if __name__ == '__main__':
    manager.run()