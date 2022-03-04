from openWzry import open_wzry
from loginWeChat import login_wechat_quit

if __name__ == '__main__':
    with open('log.txt', 'w') as f:
        f.truncate(0)
    login_wechat_quit()
    open_wzry()
