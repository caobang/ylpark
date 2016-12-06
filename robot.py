# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True)

@robot.text
def echo(message):
    return "received: %s" % message.content

