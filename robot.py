# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.replies import TextReply

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)


@robot.filter("天气")
def tianqi():
    return "晴"

@robot.filter("地图")
def ditu():
    return "226"

@robot.text
def echo(message):
    return "收到消息"

