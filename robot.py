# -*- coding: UTF-8 -*-  
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,session_storage=session_storage)

from werobot.replies import ArticlesReply, Article


@robot.text
def echo(message):
    reply = ArticlesReply(message=message)
    article = Article(
        title="WeRoBot",
        description="WeRoBot是一个微信机器人框架",
        img="https://github.com/apple-touch-icon-144.png",
        url="https://github.com/whtsky/WeRoBot"
    )
    reply.add_article(article)
    return reply

