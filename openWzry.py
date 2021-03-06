import time

from commonUtils import clickImage, print_doc, clickImageUntilItAppear
from wzryOneAccount import one_account_action


def open_wzry():
    print_doc('点击 wzry')
    clickImage('wzryIcon')
    clickImageUntilItAppear('wzryLogout')
    print_doc('点击 注销')
    print_doc('点击 同意按钮')
    clickImage('agreeButton')
    print_doc('点击 微信登录')
    clickImage('wzryLoginWechat')
    one_account_action(False)
    time.sleep(4)
    print_doc('点击 注销')
    clickImage('wzryLogout')
    print_doc('点击 同意按钮')
    clickImage('agreeButton')
    print_doc('点击 qq登录')
    clickImage('wzryLoginQQ')
    clickImageUntilItAppear('loginBlue')
    print_doc('点击 qq授权登录')
    one_account_action(True)
