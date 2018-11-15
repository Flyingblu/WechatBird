# coding=utf-8
import os
import itchat
import telepot
from telepot.loop import MessageLoop
import config
from telepot_client import *
from generic_func import *


@itchat.msg_register(itchat.content.TEXT)
def handle_text_content(msg):
    income_usr = itchat.search_friends(userName=msg['FromUserName'])
    if msg['FromUserName'] != self_usr_name:
        send = f"{contact_shower(income_usr['NickName'], income_usr['RemarkName'])}\n{msg['Content']}"
        print(wechat_bird.bot.sendMessage(config.telegramId, send))

    else:
        print("Ignored self message.")


@itchat.msg_register(itchat.content.PICTURE)
def handle_pic_content(msg):
    income_usr = msg['User']
    if msg['FromUserName'] != self_usr_name:
        send_title = f"Pic from: {contact_shower(income_usr['NickName'], income_usr['RemarkName'])}"
        msg['Text'](msg['FileName'])
        wechat_bird.bot.sendPhoto(config.telegramId, open(msg['FileName'], 'rb'))
        wechat_bird.bot.sendMessage(config.telegramId, send_title)
        os.remove(msg['FileName'])
        print(send_title + " sent")
    else:
        print("Ignored self pic")


wechat_bird = TelepotClient(telepot.Bot(config.botToken))

itchat.auto_login(hotReload=True)
MessageLoop(wechat_bird.bot,
            wechat_bird.handle_telegram_message).run_as_thread()
self_usr_name = itchat.search_friends()['UserName']
itchat.run()
