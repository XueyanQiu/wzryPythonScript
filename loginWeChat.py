import os
import time

from commonUtils import print_doc

password = ''


def input_wechat_password():
    os.system('adb shell input tap 639 1013')
    os.system('adb shell input text %s' % password)


def open_wechat():
    os.system(' adb shell am start -W -n com.tencent.mm/.plugin.account.ui.LoginPasswordUI')
    time.sleep(1)


def read_info():
    global password
    with open('wechat.txt', 'r') as f:
        data = f.readlines()
    username = data[0].strip('\n')
    password = data[1].strip('\n')


def login_wechat_quit():
    read_info()
    print_doc('点击 微信')
    open_wechat()
    time.sleep(6)
    os.system('adb shell input tap 716 1650')
    print_doc('点击 确定')
    input_wechat_password()
    print_doc('点击 登录')
    os.system('adb shell input tap 709 1457')
    time.sleep(2)
    print_doc('点击 返回桌面')
    os.system('adb shell input keyevent 3')
