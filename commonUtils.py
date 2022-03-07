from pyautogui import locateCenterOnScreen, click
import time
from PIL import ImageGrab, ImageEnhance, ImageOps

imgDocumentPath = './img/'


# click the image
def clickImage(imageName, confidence=0.7):
    location = locateCenterOnScreen(imgDocumentPath + imageName + '.png', confidence=confidence, grayscale=False)
    if location is not None:
        click(location.x, location.y, button='left')
        time.sleep(1)


# wait until the image appear, then click the image
def clickImageUntilItAppear(imageName):
    while locateCenterOnScreen(imgDocumentPath + imageName + '.png', confidence=0.7, grayscale=False) is None:
        time.sleep(1)
    clickImage(imageName)


# grab the image
def grab_image(x1: int, x2: int, y1: int, y2: int, name: str):
    print_doc('截图')
    pic = ImageGrab.grab((x1, y1, x2, y2))
    enh = ImageEnhance.Contrast(pic)
    pic = enh.enhance(3)
    pic = pic.convert('L')
    pic = ImageOps.invert(pic)
    pic.save(imgDocumentPath + name + '.png')


def print_doc(content: str):
    writestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '  ' + content + '\n'
    print(writestr)
    with open('log.txt', 'a') as logfile:
        logfile.write(writestr)
