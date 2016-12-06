# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

from werobot.replies import TextReply


@robot.text
def echo(message):
    return [
        "微信你不懂爱",
        "龚琳娜最新力作",
        "http://weixin.com/budongai.mp3",
        ]

