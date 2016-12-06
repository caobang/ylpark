from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage

session_storage = SaeKVDBStorage()
robot = WeRoBot(token="caobang", enable_session=True,
                        session_storage=session_storage)

@robot.handler
def hello(message):
    return 'hello test'

