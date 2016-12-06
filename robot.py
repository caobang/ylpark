# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
from werobot.replies import TextReply,ArticlesReply, Article

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

help = '''您好，欢迎关注\"瑶湖郊野森林公园\"
回复下列内容获取对应信息：
天气： 获取公园天气信息
交通： 获取公园交通信息
周边： 获取公园周边信息
帮助： 获取本信息'''

@robot.subscribe
def subscribe():
    return help

@robot.filter("帮助")
def ditu():
    return help

@robot.filter("天气")
def tianqi():
    reply = TextReply(message=message, content='Hello!')
    return reply
# reply.add_article(article)
#    return [
#        [
#             "瑶湖天气",
#             "",
#             "http://tu.ihuan.me/api/me_all_pic_go",
#             "http://www.caiyunapp.com/h5/?lonlat=116.056053,28.670259"
#         ]
#     ]

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

@robot.filter("周边")
def ditu():
    return [
        [
            "瑶湖周边",
            "",
            "http://tu.ihuan.me/api/me_all_pic_go",
            "http://m.amap.com/around/?locations=116.056053,28.670259&keywords=美食,酒店,地铁站,公交站&defaultIndex=1&key=54ddd5d2037636537502e1cb5e16d0a4"
        ]
    ]    

@robot.text
def echo(message):
    return "收到消息"

