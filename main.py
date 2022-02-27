import threading
import time

import pyautogui
import pytesseract
from PIL import ImageGrab, ImageEnhance, ImageOps


# back to main page
def back_to_main_page():
    while pyautogui.locateCenterOnScreen(imgDocumentPath + 'mainPageToolBar.png', confidence=0.7) is None:
        clickImage('backButton')


# click the image
def clickImage(imageName):
    location = pyautogui.locateCenterOnScreen(imgDocumentPath + imageName + '.png', confidence=0.7, grayscale=False)
    if location is not None:
        pyautogui.click(location.x, location.y, button='left')
        time.sleep(1)


# grab the image
def grab_image(x1: int, x2: int, y1: int, y2: int, name: str):
    pic = ImageGrab.grab((x1, y1, x2, y2))
    enh = ImageEnhance.Contrast(pic)
    pic = enh.enhance(3)
    pic = pic.convert('L')
    pic = ImageOps.invert(pic)
    pic.save(imgDocumentPath + name + '.png')


# 开启线程，监听页面状态点击“继续”
def clickContinueButton():
    global listenThreadRunning
    while listenThreadRunning:
        time.sleep(1)
        continueButtonLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'continueButton.png', confidence=0.7)
        if continueButtonLocation is not None:
            time.sleep(0.5)
            print('点击 继续')
            pyautogui.click(continueButtonLocation.x, continueButtonLocation.y, button='left')
    print('结束线程-点击“继续”')


# 开启线程，监听页面状态点击“确定”
def clickEnsureButton():
    global listenThreadRunning
    while listenThreadRunning:
        time.sleep(1)
        ensureButtonLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'ensureButton1.png', confidence=0.7,
                                                              grayscale=False)
        if ensureButtonLocation is None:
            ensureButtonLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'ensureButton2.png', confidence=0.7,
                                                                  grayscale=False)
        if ensureButtonLocation is None:
            ensureButtonLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'ensureButton3.png', confidence=0.7,
                                                                  grayscale=False)
        if ensureButtonLocation is not None:
            time.sleep(0.5)
            print('点击 确定')
            pyautogui.click(ensureButtonLocation.x, ensureButtonLocation.y, button='left')
    print('结束线程-点击“确定”')


# 开启线程，监听页面状态点击“挑战”
def clickChallengeButton():
    global listenThreadRunning
    while listenThreadRunning:
        time.sleep(2)
        challengeButtonLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'challengeButton.png',
                                                                 confidence=0.85, grayscale=False)
        if challengeButtonLocation is not None:
            print('点击 挑战')
            pyautogui.click(challengeButtonLocation.x, challengeButtonLocation.y, button='left')
            time.sleep(15)
    print('结束线程-点击“挑战”')


# 开启线程，监听页面状态点击“点击屏幕继续”
def clickScreenToContinue():
    global listenThreadRunning
    while listenThreadRunning:
        time.sleep(2)
        clickScreenButtonLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'clickScreenToContinue.png',
                                                                   confidence=0.7)
        if clickScreenButtonLocation is not None:
            time.sleep(0.3)
            print('点击 点击屏幕继续')
            pyautogui.click(clickScreenButtonLocation.x, clickScreenButtonLocation.y, button='left')
            time.sleep(15)
    print('结束线程-点击“点击屏幕继续”')


# 开启线程，监听页面状态点击“当前关卡”
def clickCurrentLevel():
    global listenThreadRunning
    while listenThreadRunning:
        time.sleep(2)
        clickCurrentLevelLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'currentLevel.png', confidence=0.6,
                                                                   grayscale=False)
        if clickCurrentLevelLocation is not None:
            time.sleep(0.3)
            print('点击 当前关卡')
            pyautogui.click(clickCurrentLevelLocation.x, clickCurrentLevelLocation.y, button='left')
            time.sleep(15)
    print('结束线程-点击“当前关卡”')


# 检测自动探索结束
def oneTimeExploreFinishListener():
    global listenThreadRunning
    global leftRefreshTime
    while listenThreadRunning:
        time.sleep(4)
        endTargetLocation = pyautogui.locateCenterOnScreen(imgDocumentPath + 'oneTimeExpeditionEnd.png', confidence=0.6)
        if endTargetLocation is not None:
            print('一次远征结束')
            listenThreadRunning = False
            leftRefreshTime -= 1


# 监听线程开启
def startButtonListenThread():
    try:
        thread1 = threading.Thread(target=clickChallengeButton)
        thread1.start()
        thread2 = threading.Thread(target=clickContinueButton)
        thread2.start()
        thread3 = threading.Thread(target=clickEnsureButton)
        thread3.start()
        currentLevelThread = threading.Thread(target=clickCurrentLevel)
        currentLevelThread.start()
        thread4 = threading.Thread(target=clickScreenToContinue)
        thread4.start()
        endListenerThread = threading.Thread(target=oneTimeExploreFinishListener)
        endListenerThread.start()
        thread1.join()
        thread2.join()
        thread3.join()
        currentLevelThread.join()
        thread4.join()
        endListenerThread.join()
    except:
        print("Error: 无法启动线程")


# 一次六国远征任务，从刷新开始执行
def doExpeditionOneTimeStartWithRefresh():
    refreshExplore()
    global listenThreadRunning
    listenThreadRunning = True
    startButtonListenThread()


# 刷新六国远征并开启自动探索
def refreshExplore():
    print('点击 立即重置')
    clickImage('refreshExpedition')
    clickImage('ensureButton1')
    time.sleep(1)
    print('点击 自动探索')
    clickImage('autoExplore')


# 右下角小妲己接收所有礼物
def getDajiReward():
    print('点击 妲己')
    clickImage('harvestRewards1')
    clickImage('harvestRewards2')
    print('点击 去领取')
    clickImage('getRewards')
    print('点击 收下')
    clickImage('acceptRewards')
    time.sleep(2)
    print('点击 确定')
    clickImage('ensureButton2')
    print('点击 返回')
    clickImage('backButton')


# 当前六国远征刷新次数位置进行截图，提高对比度，转换为灰度图，色彩反转后，保存。图案最终为白底黑字方便ocr识别
def grab_expedition_rest_time():
    refreshImgLocation = pyautogui.locateOnScreen(imgDocumentPath + 'todayLastExploreTimeText.png')
    if refreshImgLocation is None:
        return False
    else:
        x1 = refreshImgLocation[0] + refreshImgLocation[2]
        y1 = refreshImgLocation[1] - refreshImgLocation[3] * 0.4
        x2 = refreshImgLocation[0] + refreshImgLocation[2] * 1.4
        y2 = refreshImgLocation[1] + refreshImgLocation[3] * 1.4
        grab_image(x1, x2, y1, y2, 'restTimeGrab')
        return True


# 使用pytesseract ocr识别当前六国远征剩余刷新次数
def get_rest_explore_time():
    if grab_expedition_rest_time():
        last_time = pytesseract.image_to_string(imgDocumentPath + 'restTimeGrab.png', lang='chi_sim',
                                                config=' --psm 7 --oem 3 -c tessedit_char_whitelist=01234').strip()
        print('剩余远征刷新次数： ' + last_time)
        return int(last_time)
    else:
        return 0


# 进入邮箱并接受所有邮件的附件
def get_emails():
    print('点击 邮箱')
    clickImage('messageBox')
    print('点击 系统邮件')
    clickImage('systemEmails')
    print('点击 立即领取')
    clickImage('getSystemEmailAttachments')
    while pyautogui.locateCenterOnScreen(imgDocumentPath + 'ensureButton2.png', confidence=0.8) is not None:
        clickImage('ensureButton2')
        time.sleep(0.5)
    print('点击 好友邮件')
    clickImage('friendEmails')
    print('点击 立即领取')
    clickImage('getSystemEmailAttachments')
    while pyautogui.locateCenterOnScreen(imgDocumentPath + 'ensureButton2.png', confidence=0.8) is not None:
        clickImage('ensureButton2')
        time.sleep(0.5)
    print('点击 返回')
    clickImage('backButton')


# 进入六国远征
def enter_expedition():
    clickImage('expeditionEntrence1')
    time.sleep(0.6)
    clickImage('expeditionEntrence2')
    clickImage('expeditionEntrence3')


# 开启六国远征
def start_expedition():
    enter_expedition()
    while get_rest_explore_time() != 0:
        if not listenThreadRunning:
            doExpeditionOneTimeStartWithRefresh()


# 进入武道大会
def enter_rank_meeting():
    clickImage('expeditionEntrence1')
    time.sleep(0.6)
    clickImage('expeditionEntrence2')
    clickImage('rankMeetingEntrance')


# 开启武道大会
def start_rank_meeting():
    enter_rank_meeting()
    while get_rest_rank_meeting_time() > 0:
        rank_meeting_challenge_once()


# 当前武道大会刷新次数位置进行截图，提高对比度，转换为灰度图，色彩反转后，保存。图案最终为白底黑字方便ocr识别
def grab_rank_meeting_rest_time():
    refreshChallengerImgLocation = pyautogui.locateOnScreen(imgDocumentPath + 'refreshChallenger.png')
    if refreshChallengerImgLocation is None:
        return False
    else:
        print(refreshChallengerImgLocation)
        x1 = refreshChallengerImgLocation[0] - refreshChallengerImgLocation[2] * 0.535
        x2 = refreshChallengerImgLocation[0]
        y1 = refreshChallengerImgLocation[1]
        y2 = refreshChallengerImgLocation[1] + refreshChallengerImgLocation[3]
        grab_image(x1, x2, y1, y2, 'restRankTimeGrab')
        return True


# 使用pytesseract ocr识别当前武道大会剩余刷新次数
# 不能识别出符号/，会识别成1，因此要判断前两位
def get_rest_rank_meeting_time():
    if grab_rank_meeting_rest_time():
        last_time = pytesseract.image_to_string(imgDocumentPath + 'restRankTimeGrab.png', lang='chi_sim',
                                                config=' --psm 7 --oem 3 -c tessedit_char_whitelist=0123456789').strip()
        res = 0
        if last_time[0] == '1' and last_time[1] == '0':
            res = 10
        elif last_time[1] == '1':
            res = int(last_time[0])
        print('剩余武道大会刷新次数： ' + str(res))
        return res
    else:
        return 0


# 开始一次武道大会挑战
def rank_meeting_challenge_once():
    refreshChallengerImgLocation = pyautogui.locateOnScreen(imgDocumentPath + 'refreshChallenger.png', confidence=0.7)
    click_challenge_pos_x = refreshChallengerImgLocation[0] + refreshChallengerImgLocation[2] * 0.5
    click_challenge_pos_y = refreshChallengerImgLocation[1] - refreshChallengerImgLocation[3] * 2
    print('点击 挑战三名中的最后一个')
    pyautogui.click(click_challenge_pos_x, click_challenge_pos_y, button='left')
    print('点击 挑战')
    clickImage('challengeButton')
    print('点击 确定')
    clickImage('ensureButton1')
    while pyautogui.locateCenterOnScreen(imgDocumentPath + 'clickScreenToContinue.PNG', confidence=0.7) is None:
        time.sleep(1)
    print('点击 点击屏幕继续')
    clickImage('clickScreenToContinue')
    print('点击 继续')
    clickImage('continueButton')
    print('点击 屏幕任意位置')
    clickImage('clickScreenToContinue2')
    print('点击 继续')
    clickImage('continueButton')


# 关闭开屏广告
def close_start_game_ad():
    for i in range(6):
        clickImage('closeAd')


# 点击开始游戏
def click_start_game():
    print('点击 开始游戏')
    clickImage('startGame')
    time.sleep(5)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    imgDocumentPath = './img/'
    listenThreadRunning = False
    click_start_game()
    close_start_game_ad()
    get_emails()
    getDajiReward()
    start_expedition()
    back_to_main_page()
    start_rank_meeting()

