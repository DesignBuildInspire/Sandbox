from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS

import time


# instantiate and register the cmd handler

board = Arduino("/dev/tty.usbserial-1430",baudrate=115200)


iterator = util.Iterator(board)
iterator.start()
board.digital[13].write(1)
time.sleep(1)
board.digital[13].write(0)

