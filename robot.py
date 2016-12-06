# -*- coding: UTF-8 -*-  
from werobot import WeRoBot

robot = WeRoBot(token="caobang")

@robot.text
def echo(message):
    return "received: %s" % message.content

