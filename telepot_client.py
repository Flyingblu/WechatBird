import telepot

class TelepotClient:
    def __init__(self, telepot_bot):
        self.flag = [0, 0]
        self.usr_name = 'filehelper'
        self.usr_nick = 'FileHelper'
        self.usr_remark = ''
        self.wechatBird = telepot_bot

    def handle_telegram_message(msg):
        nonlocal flag, usr_name, usr_nick, usr_remark
        if msg['text'][0] == '/':
            if msg['text'] == r'/settalkto':
                flag[0] = 1
                wechatBird.sendMessage(Config.telegramId, "I'm fetching data, please wait ~")
                print("Begin fetching current contact")
                friends = itchat.get_friends(update=True)
                buttons = []
                for i in range(1, 10):
                    buttons.append(
                        [namedtuple.KeyboardButton(
                            text=f"{i}: {contact_shower(friends[i]['NickName'], friends[i]['RemarkName'])}")])
                wechatBird.sendMessage(Config.telegramId, "Here's your current contact😊",
                                       reply_markup=namedtuple.ReplyKeyboardMarkup(keyboard=buttons))
                print("Fetched current contact")

            elif msg['text'] == r'/currenttalkto':
                wechatBird.sendMessage(Config.telegramId,
                                       f"Currently you are talking to {contact_shower(usr_nick, usr_remark)}")
                print(f"Displayed current talk to {contact_shower(usr_nick, usr_remark)}")

            elif msg['text'] == r'/searchfriend':
                flag[1] = 1
                wechatBird.sendMessage(Config.telegramId, "Please tell me your friend's nickname or remark name")
                print("Ready to search friend")
            # Under construction!

            else:
                wechatBird.sendMessage(Config.telegramId, "Please give me a correct command😂")
                print("User command error")

        else:
            if flag[0]:
                flag[0] = 0
                try:
                    no = msg['text'][0]
                    usr = itchat.get_friends()[int(no)]
                    usr_name = usr['UserName']
                    usr_nick = usr['NickName']
                    usr_remark = usr['RemarkName']
                    wechatBird.sendMessage(Config.telegramId,
                                           f"You're now talking to {contact_shower(usr_nick, usr_remark)}!",
                                           reply_markup=namedtuple.ReplyKeyboardRemove())
                    print(f"Set talk to {contact_shower(usr_nick, usr_remark)}")

                except:
                    wechatBird.sendMessage(Config.telegramId, "Oops, your command seems incorrect😂",
                                           reply_markup=namedtuple.ReplyKeyboardRemove())
                    print("User command error")

            elif flag[1]:
                flag[1] = 0
                found_friend = itchat.search_friends(name=msg['text'])
                if found_friend:
                    usr_name = found_friend[0]['UserName']
                    usr_nick = found_friend[0]['NickName']
                    usr_remark = found_friend[0]['RemarkName']
                    wechatBird.sendMessage(Config.telegramId,
                                           f"You're now talking to {contact_shower(usr_nick, usr_remark)}!")
                    print(f"Set talk to {contact_shower(usr_nick, usr_remark)}")

                else:
                    wechatBird.sendMessage(Config.telegramId, "Sorry, friend not found")
                    print("Friend not found")

            else:
                itchat.send(msg['text'], toUserName=usr_name)
                wechatBird.sendMessage(Config.telegramId, f"Message sent to {contact_shower(usr_nick, usr_remark)}")
                print(f"Message sent to {contact_shower(usr_nick, usr_remark)}")

    return handle_telegram_message