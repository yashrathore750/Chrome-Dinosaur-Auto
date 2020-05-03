import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def Colliding(data):
    for i in range(250,300):
            for j in range(470,580):
                if data[i,j] < 100:
                    hit("down")
                    return                
    for i in range(400,700):
            for j in range(410,700):
                if data[i,j] < 100:
                    hit("up")
                    return                 
    return 
   
if __name__ == "__main__":
    print("Game starting")
    time.sleep(2)
    hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        Colliding(data)
       

                