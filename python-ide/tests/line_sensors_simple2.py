# SIGUELINEAS FUNCIONAL, TENEMOS INTEARICTIVIDAD AL PULSAR EL BOTON A
from microbit import *
import lib_robot_maqueen as mqn
import time #can be removed if not used
from music import pitch
mq = mqn.MaqueenPlus()

dir = 1 #hacia adelante, atras: 2
leftSpeed  = 60
rightSpeed = 60
ordered_keys = ["L3", "L2", "L1", "R1", "R2", "R3"]
TURN_SCALE = 40

def calculate_error():
    # Assign weights to each sensor to calculate the error value
    weights = [-3, -2, -1, 1, 2, 3]
    error = 0


    # Calculate weighted error based on sensor states
    for i in range(6):
        if sens_list[i] == 1:  # Sensor detects the line
            error += weights[i]
    
    return error * TURN_SCALE #Optimizar multiplicando los valores de los pesos directamente

display.show(Image.HEART)
while True:
    mq.motorControl(mq.MT_L,dir,leftSpeed)
    mq.motorControl(mq.MT_R,dir,rightSpeed)
    line = mq.getLine() #devuelve un diccionario con keys "L1", "R3"... y valor
    #0: white, 1: black
    
    sens_list = [line[key] for key in ordered_keys]
    error = calculate_error()
    leftSpeed = min(max(120 - error, 0), 255)
    rightSpeed = min(max(120 + error, 0), 255)
    display.show(Image.ANGRY)

    if(button_a.was_pressed()):
        mq.stop()
        display.show(Image.HEART)
        pitch(340 + error, 100)
