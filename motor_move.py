from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS

import time

# instantiate and register the cmd handler

board = Arduino("/dev/tty.usbserial-1410",baudrate=115200)

iterator = util.Iterator(board)
iterator.start()

# Dir1 pin on mCore is D7
board.digital[7].write(0)
# Dir1 pin on mCore is D4
board.digital[4].write(1)

motor1_pwm = board.digital[5]
motor1_pwm.mode = PWM
motor2_pwm = board.digital[6]
motor2_pwm.mode = PWM

motor1_pwm.write(0.5)
motor2_pwm.write(0.5)
time.sleep(2)
motor1_pwm.write(0)
motor2_pwm.write(0)


