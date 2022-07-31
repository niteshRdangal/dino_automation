import time
import pyautogui
from PIL import Image, ImageGrab
from numpy import asarray 

def hit(key):
    pyautogui.keyDown(key)

def draw():
    pass

def cactusComming(data):
    for i in range(300,420):
            for j in range(605,657):
                if data[i, j] >150:
                    return True
    return False



if __name__ == "__main__":
    print("The game is about to start")
    time.sleep(3)
    hit("up")
    while True:
        image =  ImageGrab.grab().convert('L') # converted the imgae into grayscale
        data = image.load() 
        if cactusComming(data):
            hit("up")
        #print(asarray(image)) # numpy asarray stored the image in array form
        # for i in range(300,420):
        #     for j in range(605,657):
        #         data[i, j] = 255

        #image.show()
    