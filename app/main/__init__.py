# -*- coding: UTF-8 -*-
from flask import Blueprint
route = Blueprint('main', __name__)
from . import views, errors