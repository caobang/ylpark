# -*- coding: UTF-8 -*-  
from werobot.robot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.replies import TextReply

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

@robot.text
def echo(message):
    return "收到消息"

