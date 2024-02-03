from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT, OUTPUT
from pyfirmata.boards import BOARDS

import time, sys
import serial.tools.list_ports, time
# numbers = 
zero = (0,0,0,0,0,0,1)
one = (1,0,0,1,1,1,1)
two = (0,0,1,0,0,1,0)
three = (0,0,0,0,1,1,0)
four = (1,0,0,1,1,0,0)
five = (0,1,0,0,1,0,0)
six = (0,1,0,0,0,0,0)
seven = (0,0,0,1,1,1,1)
eight = (0,0,0,0,0,0,0)
nine = (0,0,0,0,1,0,0)

print ( type (zero))


def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))

# instantiate and register the cmd handler

board = Arduino(get_mbot_port(),baudrate=115200)

iterator = util.Iterator(board)
iterator.start()


a = board.digital[23] # pin 11 of 7 seg display 
b = board.digital[22] # pin 7  of 7 seg display 
c = board.digital[21] # pin 4  of 7 seg display 
d = board.digital[19] # pin 2  of 7 seg display 
e = board.digital[18] # pin 1  of 7 seg display 
f = board.digital[5]  # pin 10 of 7 seg display 
g = board.digital[4]  # pin 5  of 7 seg display 

a.mode = OUTPUT
b.mode = OUTPUT
c.mode = OUTPUT
d.mode = OUTPUT
e.mode = OUTPUT
f.mode = OUTPUT
g.mode = OUTPUT


def print_7seg(input):
    global a,b,c,d,e,f,g
    
    a.write(input[0])
    b.write(input[1])
    c.write(input[2])
    d.write(input[3])
    e.write(input[4])
    f.write(input[5])
    g.write(input[6])


a.write(1)


while True:
    print_7seg(zero)
    time.sleep(1)
    print_7seg(one)
    time.sleep(1)
    print_7seg(two)
    time.sleep(1)
    print_7seg(three)
    time.sleep(1)
    print_7seg(four)
    time.sleep(1)
    print_7seg(five)
    time.sleep(1)
    print_7seg(six)
    time.sleep(1)
    print_7seg(seven)
    time.sleep(1)
    print_7seg(eight)
    time.sleep(1)
    print_7seg(nine)
    time.sleep(1)
