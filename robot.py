# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

@robot.text
def echo(message):
    return [
        [
            "title",
            "description",
            "img",
            "url"
        ],
        [
            "whtsky",
            "I wrote WeRoBot",
            "https://secure.gravatar.com/avatar/0024710771815ef9b74881ab21ba4173?s=420",
            "http://whouz.com/"
        ]
    ]

