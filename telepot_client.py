import telepot
import itchat
import config
from telepot import namedtuple
from generic_func import *


class TelepotClient:
    def __init__(self, telepot_bot):
        self.status = 0
        '''
            status: bot 的 command 的设定状态。
            1 = /settalkto
            2 = /searchfriend
        '''
        self.usr_name = 'filehelper'
        self.usr_nick = 'FileHelper'
        self.usr_remark = ''
        self.bot = telepot_bot

    def set_talk_to(self):
        self.status = 1
        self.bot.sendMessage(config.telegramId,
                             "I'm fetching data, please wait ~")
        print("Begin fetching current contact")
        friends = itchat.get_friends(update=True)
        buttons = []
        for i in range(1, 10):
            buttons.append([
                namedtuple.KeyboardButton(
                    text=
                    f"{i}: {contact_shower(friends[i]['NickName'], friends[i]['RemarkName'])}"
                )
            ])
        self.bot.sendMessage(
            config.telegramId,
            "Here's your current contact😊",
            reply_markup=namedtuple.ReplyKeyboardMarkup(keyboard=buttons))
        print("Fetched current contact")

    def current_talk_to(self):
        self.bot.sendMessage(
            config.telegramId,
            f"Currently you are talking to {contact_shower(self.usr_nick, self.usr_remark)}"
        )
        print(
            f"Displayed current talk to {contact_shower(self.usr_nick, self.usr_remark)}"
        )

    def search_friend(self):
        self.status = 2
        self.bot.sendMessage(
            config.telegramId,
            "Please tell me your friend's nickname or remark name")
        print("Ready to search friend")

    def select_friend(self, msg):
        self.status = 0
        try:
            no = msg['text'][0]
            usr = itchat.get_friends()[int(no)]
            self.usr_name = usr['UserName']
            self.usr_nick = usr['NickName']
            self.usr_remark = usr['RemarkName']
            self.bot.sendMessage(
                config.telegramId,
                f"You're now talking to {contact_shower(self.usr_nick, self.usr_remark)}!",
                reply_markup=namedtuple.ReplyKeyboardRemove())
            print(
                f"Set talk to {contact_shower(self.usr_nick, self.usr_remark)}"
            )

        except:
            self.bot.sendMessage(
                config.telegramId,
                "Oops, your command seems incorrect😂",
                reply_markup=namedtuple.ReplyKeyboardRemove())
            print("User command error")

    def search_friend_by_input(self, msg):
        self.status = 0
        found_friend = itchat.search_friends(name=msg['text'])
        if found_friend:
            self.usr_name = found_friend[0]['UserName']
            self.usr_nick = found_friend[0]['NickName']
            self.usr_remark = found_friend[0]['RemarkName']
            self.bot.sendMessage(
                config.telegramId,
                f"You're now talking to {contact_shower(self.usr_nick, self.usr_remark)}!"
            )
            print(
                f"Set talk to {contact_shower(self.usr_nick, self.usr_remark)}"
            )

        else:
            self.bot.sendMessage(config.telegramId, "Sorry, friend not found")
            print("Friend not found")

    def handle_telegram_message(self, msg):
        if msg['text'][0] == '/':
            if msg['text'] == r'/settalkto':
                self.set_talk_to()

            elif msg['text'] == r'/currenttalkto':
                self.current_talk_to()

            elif msg['text'] == r'/searchfriend':
                self.search_friend()

            else:
                self.bot.sendMessage(config.telegramId,
                                     "Please give me a correct command😂")
                print("User command error")

        else:
            if self.status == 1:
                self.select_friend(msg)

            elif self.status == 2:
                self.search_friend_by_input(msg)

            else:
                itchat.send(msg['text'], toUserName=self.usr_name)
                self.bot.sendMessage(
                    config.telegramId,
                    f"Message sent to {contact_shower(self.usr_nick, self.usr_remark)}"
                )
                print(
                    f"Message sent to {contact_shower(self.usr_nick, self.usr_remark)}"
                )
