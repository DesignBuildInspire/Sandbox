from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT, OUTPUT
from pyfirmata.boards import BOARDS

import time, sys, threading
import serial.tools.list_ports, time
numbers = (
    (0,0,0,0,0,0,1),
    (1,0,0,1,1,1,1),
    (0,0,1,0,0,1,0),
    (0,0,0,0,1,1,0),
    (1,0,0,1,1,0,0),
    (0,1,0,0,1,0,0),
    (0,1,0,0,0,0,0),
    (0,0,0,1,1,1,1),
    (0,0,0,0,0,0,0),
    (0,0,0,0,1,0,0))

map_p = (23,22,21,19,18,5,4)
id_p = (2,15)

print (map_p.__sizeof__())

def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))

# instantiate and register the cmd handler

board = Arduino(get_mbot_port(),baudrate=115200)
iterator = util.Iterator(board)
iterator.start()

for i in range(7): 
    board.digital[map_p[i]].mode = OUTPUT
    board.digital[map_p[i]].write(1)  

for i in range(2): 
    board.digital[id_p[i]].mode = OUTPUT
    board.digital[id_p[i]].write(1)  

def print_7seg(board,input):
    global map_p
    for i in range(7): 
        board.digital[map_p[i]].write(input[i])

while True:
    board.digital[id_p[0]].write(1)
    board.digital[id_p[1]].write(0)
    print_7seg(board,numbers[5])
    time.sleep(.5)
    board.digital[id_p[0]].write(0)
    board.digital[id_p[1]].write(1)
    print_7seg(board,numbers[6])
    time.sleep(.5)

# for i in range (10):
#     print_7seg(board, numbers[i])
#     time.sleep(0.5)
