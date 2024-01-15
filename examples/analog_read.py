from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS

import time

# instantiate and register the cmd handler

board = Arduino("/dev/tty.usbserial-1410",baudrate=115200)

iterator = util.Iterator(board)
iterator.start()


# analog_1 = board.analog[0]
# analog_1.mode = ANALOG
# analog_1.read()

# pin_number = 2
# board.analog[pin_number].enable_reporting()

# while True : 
#     print (board.analog[pin_number].read())
#     time.sleep(.1)    



