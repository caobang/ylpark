# -*- coding: UTF-8 -*-
from . import route
from robot import robot
from werobot.contrib.flask import make_view

route.add_url_rule(rule='/',
                 endpoint='werobot',
                 view_func=make_view(robot),
                 methods=['GET', 'POST'])