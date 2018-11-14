# coding=utf-8
import itchat
import telepot
from telepot import namedtuple
from telepot.loop import MessageLoop
import config
from telepot_client import *
from generic_func import *


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    incomeUsr = itchat.search_friends(userName=msg['FromUserName'])
    if not incomeUsr['Uin']:
        send = f"{contact_shower(incomeUsr['NickName'], incomeUsr['RemarkName'])}\n{msg['Content']}"
        print(wechat_bird.bot.sendMessage(config.telegramId, send))

    else:
        print("Ignored self message.")


wechat_bird = TelepotClient(telepot.Bot(config.botToken))

itchat.auto_login(hotReload=True)
MessageLoop(wechat_bird.bot,
            wechat_bird.handle_telegram_message).run_as_thread()
itchat.run()
