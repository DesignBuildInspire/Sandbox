from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT, OUTPUT
from pyfirmata.boards import BOARDS

import time
import serial.tools.list_ports, time


def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))

# instantiate and register the cmd handler

board = Arduino(get_mbot_port(),baudrate=115200)

iterator = util.Iterator(board)
iterator.start()

board.digital[2].mode = OUTPUT

# print(board.get_firmata_version())
def blinkled(count,delay=0.2):
    for x in range(count):
        board.digital[2].write(1)
        time.sleep(delay)
        board.digital[2].write(0)
        time.sleep(delay)
        
# try:
#     number=int(input("enter number"))
#     print(number)
# except ValueError:
#     print("There is a value error")      

  
blinkled(5)