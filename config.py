# -*- coding: UTF-8 -*- 
from werobot import WeRoBot
from werobot.session.saekvstorage import SaeKVDBStorage
session_storage = SaeKVDBStorage()
Config = dict(
    TOKEN="caobang",
    SESSION_STORAGE=session_storage,
    APP_ID=None,
    APP_SECRET=None,
    ENCODING_AES_KEY=None
)