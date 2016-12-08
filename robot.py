# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from config import Config
from werobot.replies import TextReply,ArticlesReply, Article
import time
import urllib2

robot = WeRoBot(enable_session=False)
robot.config.from_object(Config)

help = '''您好，欢迎关注\"瑶湖郊野森林公园\"
回复下列文字或数字获取对应信息：
天气(1)： 获取公园天气信息
交通(2)： 获取公园交通信息
周边(3)： 获取公园周边信息
美图(4)： 获取必应今日美图
帮助(0)： 获取本信息'''

@robot.subscribe
def subscribe():
    return help

@robot.filter("帮助","0")
def ditu():
    return help

@robot.filter("天气","1")
def tianqi():
    return [
        [
            "瑶湖天气",
             "",
             "http://tu.ihuan.me/api/me_all_pic_go?t=%s" % time.time(),
             "http://www.caiyunapp.com/h5/?lonlat=116.056053,28.670259"
         ]
    ]

@robot.filter("交通","2")
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

@robot.filter("周边","3")
def ditu():
    return [
        [
            "瑶湖周边",
            "",
            "http://tu.ihuan.me/api/me_all_pic_go?t=%s" % time.time(),
            "http://m.amap.com/around/?locations=116.056053,28.670259&keywords=美食,酒店,地铁站,公交站&defaultIndex=1&key=54ddd5d2037636537502e1cb5e16d0a4"
        ]
    ]

@robot.filter("美图","4")
def ditu():
    return [
        [
            "必应今日美图",
            urllib2.urlopen("http://tu.ihuan.me/tu/api/bing/text?t=%s" % time.time()).read(),
            "http://tu.ihuan.me/api/bing/go?t=%s" % time.time(),
            "http://cn.bing.com/images/trending"
        ]
    ]

@robot.text
def echo(message):
    return "收到消息"
