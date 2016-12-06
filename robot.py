# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.replies import TextReply

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)


@robot.filter("天气")
def tianqi():
    return [
        [
            "瑶湖天气",
            "【当前】晴",
            "img",
            "url"
        ],
        [
            "whtsky",
            "I wrote WeRoBot",
            "https://mmbiz.qlogo.cn/mmbiz/kic6WM8B8jd41FXzEMpTpxRe8HIMUOeTyHrsBFjkyL26ObwMEGhdOYLiaRCyvH0iahpgABLRsCk5sbezbBbWaXTibQ/0?wx_fmt=jpeg",
            "http://www.caiyunapp.com/h5/?lonlat=116.056053,28.670259"
        ]
    ]

@robot.filter("地图")
def ditu():
    return "226"

@robot.text
def echo(message):
    return "收到消息"

