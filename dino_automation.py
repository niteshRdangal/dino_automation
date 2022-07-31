import time
import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray 

def hit(key):
    pyautogui.keyDown(key)


def draw():
    pass

def screenShot():
    image =  ImageGrab.grab().convert('L')
    return image


if __name__ == "__main__":
    time.sleep(1)
    image = screenShot()
    data = image.load() 
    print(asarray(image))
    for i in range(34,45):
        for j in range(45,67):
            data
    