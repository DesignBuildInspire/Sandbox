from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT, OUTPUT
from pyfirmata.boards import BOARDS

import time, sys, threading
import serial.tools.list_ports, time


map_p = (23,22,21,19,18,5,4,2)
id_p = (2,15)
col=[]
row=[]

# print (map_p.__sizeof__())

def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))

# instantiate and register the cmd handler

board = Arduino(get_mbot_port(),baudrate=115200)
iterator = util.Iterator(board)
iterator.start()



for i in range(0,4):
    col.append(board.digital[map_p[i]])

for i in range(4,8):
    row.append(board.digital[map_p[i]])
    
for i in range(0,4):
    col[i].mode = OUTPUT
    col[i].write(0)  
    row[i].mode = OUTPUT
    row[i].write(0)  
    

def set_point (x,y):
    for i in range(0,4):
        if (i==x):
            col[i].write(1)
        else:
            col[i].write(0)
        if (i==y):
            row[i].write(0)
        else:
            row[i].write(1)

def clear_all():
    for i in range(0,4):
        col[i].write(0)  
        row[i].write(0)  

def clear_point (x,y):
    if (x<4):
        col[x].write(0)
    if (y<4):
        row[y].write(0)
      
      
# for i in range (4):
#     for j in range(4):
#         set_point(i,j)
#         time.sleep(0.25)

while True:
    set_point(0,0)
    time.sleep(0.05)
    clear_point(0,0)
    set_point(1,1)
    clear_point(1,1)
    time.sleep(1,1)