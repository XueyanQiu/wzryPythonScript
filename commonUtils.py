from pyautogui import locateCenterOnScreen, click
import time
from PIL import ImageGrab, ImageEnhance, ImageOps


imgDocumentPath = './img/'


# click the image
def clickImage(imageName):
    location = locateCenterOnScreen(imgDocumentPath + imageName + '.png', confidence=0.7, grayscale=False)
    if location is not None:
        click(location.x, location.y, button='left')
        time.sleep(1)


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
    with open('log.txt', 'a') as logfile:
        logfile.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '  ' + content + '\n')