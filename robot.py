# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.replies import TextReply

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

help = '''您好，欢迎关注\"瑶湖郊野森林公园\"
回复下列内容获取对应信息：
天气： 获取公园附近天气信息
交通： 获取公园交通信息
帮助： 获取本信息'''

@robot.subscribe
def subscribe():
    return help

@robot.filter("帮助")
def ditu():
    return help

@robot.filter("天气")
def tianqi():
    return [
        [
            "瑶湖天气",
            "",
            "https://mmbiz.qlogo.cn/mmbiz/kic6WM8B8jd41FXzEMpTpxRe8HIMUOeTyHrsBFjkyL26ObwMEGhdOYLiaRCyvH0iahpgABLRsCk5sbezbBbWaXTibQ/0?wx_fmt=jpeg",
            "http://www.caiyunapp.com/h5/?lonlat=116.056053,28.670259"
        ]
    ]

@robot.filter("交通")
def ditu():
    return [
        [
            "选择您的出行方式",
            "",
            "",
            ""
        ],
        [
            "驾车",
            "",
            "",
            "http://m.amap.com/navi/?dest=116.056053,28.670259&destName=%E7%91%B6%E6%B9%96%E9%83%8A%E9%87%8E%E6%A3%AE%E6%9E%97%E5%85%AC%E5%9B%AD&naviBy=car&key=54ddd5d2037636537502e1cb5e16d0a4"
        ],
        [
            "公交",
            "",
            "",
            "http://m.amap.com/navi/?dest=116.056053,28.670259&destName=%E7%91%B6%E6%B9%96%E9%83%8A%E9%87%8E%E6%A3%AE%E6%9E%97%E5%85%AC%E5%9B%AD&naviBy=bus&key=54ddd5d2037636537502e1cb5e16d0a4"
        ],
        [
            "步行",
            "",
            "",
            "http://m.amap.com/navi/?dest=116.056053,28.670259&destName=%E7%91%B6%E6%B9%96%E9%83%8A%E9%87%8E%E6%A3%AE%E6%9E%97%E5%85%AC%E5%9B%AD&naviBy=walk&key=54ddd5d2037636537502e1cb5e16d0a4"
        ]
    ]    

@robot.text
def echo(message):
    return "收到消息"

