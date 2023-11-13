from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS

import time


# instantiate and register the cmd handler

board = Arduino("/dev/tty.usbserial-1410",baudrate=115200)


iterator = util.Iterator(board)
iterator.start()

port =''
pin = 11

board.digital[pin].mode = SERVO


# print(board.get_firmata_version())

    
def rotate_servo(pin, angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)


while True:
    for i in range(0,180):
        rotate_servo(pin,i)
    for i in range(180,1,-1):
        rotate_servo(pin,i)   
