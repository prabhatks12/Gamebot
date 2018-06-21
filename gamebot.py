# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 22:04:02 2018

@author: prabhat
"""

import numpy as np
from PIL import ImageGrab,ImageOps
import pyautogui as py
import time

class coordinate():
    replayBtn=(330,360)
    dinosaur=(170,400)
    #tree height x coordinate 260
    #y coordinae 420

def restartGame():
        py.click(coordinate.replayBtn)

def pressSpace():
    py.keyDown('space')
    time.sleep(0.05)
    print("jump")
    py.keyUp('space')

def imageGrab():    
    #creatin a box from box(x1,y1,y2,y2) from x1,x2 it checks for ground obstackles and from y1 to y2 flying obstackles
    box=(coordinate.dinosaur[0]+60,coordinate.dinosaur[1],coordinate.dinosaur[0]+80,coordinate.dinosaur[1]+10)
    image=ImageGrab.grab(box)
    grayImage=ImageOps.grayscale(image)
    a=np.array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

i=0   

def main():
    restartGame()  #when we have restart button
    pressSpace()   #when we dont have restart button
    while True:
        if imageGrab()!=447 :
            pressSpace()
            time.sleep(0.1)

main()   

"""

restartGame()
time.sleep(1)
pressSpace()

#finding the x1 and x2 coordinates

while True:
    imageGrab()  
"""      
        

