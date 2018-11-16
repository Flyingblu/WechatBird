# coding=utf-8
from PIL import Image


def contact_shower(nick_name, remark_name=""):
    if remark_name != "":
        return f"{remark_name} ({nick_name})"
    else:
        return nick_name


def inspect_pic(file_name):
    try:
        with Image.open(file_name) as pic:
            print(pic.format, "%dx%d" % pic.size, pic.mode)
            return pic.format, pic.size

    except IOError:
        print("IOError when opening pic!")
