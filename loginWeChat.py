import time

from commonUtils import clickImage, print_doc, clickImageUntilItAppear
from pyautogui import press

password = ''


def input_wechat_password():
    clickImage('wechatPassword2')
    for char in password:
        press(char)
        time.sleep(0.2)


def open_wechat():
    clickImage('wechatIcon')
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
    clickImageUntilItAppear('wechatEnsure')
    print_doc('点击 确定')
    input_wechat_password()
    print_doc('点击 登录')
    clickImage('loginGreen')
    time.sleep(2)
    print_doc('点击 返回桌面')
    clickImage('backToDesktop')
