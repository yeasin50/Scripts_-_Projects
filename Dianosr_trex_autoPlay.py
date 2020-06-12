from numpy import *
from pil  import ImageGrab, ImageOps
import pyautogui
import time
from numpy.ma import array

'''
website : http://www.trex-game.skipser.com/
my screen size : 1920 *1080
using right half of screen for dinasor game , other one to run code 
you can use paintdot software to find the coordinates 
'''


class Cordinate():
    #find reply button , 
    replyBtn = (480,402)
    dinasor = (246, 406)

    # chk tree x=244 y=430
    

def restartGame():
    pyautogui.click(Cordinate.replyBtn)

def pressSpace():
    pyautogui.keyDown("space")
    #maintain Jump 
    time.sleep(0.005)
    print("Jumped")
    pyautogui.keyUp("space")

def imageGRab():
    # find the rectange of object to jump acction
    box = (246, 390, 350,420)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()


def main():
    restartGame()

    while True:
        print(imageGRab())
        #modify value accordingly 
        if(imageGRab()!=3367):
            pressSpace()
            

main()
