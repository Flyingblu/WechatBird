# coding=utf-8
def contact_shower(nick_name, remark_name=""):
    if remark_name != "":
        return f"{remark_name} ({nick_name})"
    else:
        return nick_name
