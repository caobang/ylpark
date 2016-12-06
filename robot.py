# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.replies import TextReply

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

help = '''你好，欢迎关注\"瑶湖郊野森林公园\"
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
    return '''自驾路线：驾车上瑶湖大桥，到瑶湖大桥桥头有加油站，即可看到瑶湖森林公园停车场导向标识。
公交车：乘坐“226路“到瑶湖大酒店（加油站）或后埔尚村站对面直达瑶湖森林公园
乘坐”258路“到后埔尚村下车对面直达瑶湖森林公园'''

@robot.text
def echo(message):
    return "收到消息"

