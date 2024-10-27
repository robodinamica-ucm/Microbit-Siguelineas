# Imports go at the top
from microbit import *
import lib_robot_maqueen as mqn
import time #can be removed if not used
from music import pitch
mq = mqn.MaqueenPlus()

dir = 1 #hacia adelante, atras: 2
leftSpeed  = 60
rightSpeed = 60

display.show(Image.HEART)

while True:
    mq.motorControl(mq.MT_L,dir,leftSpeed)
    mq.motorControl(mq.MT_R,dir,rightSpeed)
    line = mq.getLine() #devuelve un diccionario con keys "L1", "R3"... y valor
    #0: white, 1: black
    ordered_keys = ["L3", "L2", "L1", "R1", "R2", "R3"]
    sens_list = [line[key] for key in ordered_keys]
    leftSpeed = min(max(sens_list[0]*100, 0), 255)
    rightSpeed = min(max(sens_list[5]*100, 0), 255)
    display.show(Image.ANGRY)

    if(button_a.was_pressed()):
        mq.stop()
        display.show(Image.HEART)
