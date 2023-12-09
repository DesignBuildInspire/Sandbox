from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT
from pyfirmata.boards import BOARDS

import time


# instantiate and register the cmd handler

board = Arduino("/dev/tty.usbserial-1430",baudrate=115200)

iterator = util.Iterator(board)
iterator.start()













# print(board.get_firmata_version())
def blinkled(count,delay=0.2):
    for x in range(count):
        board.digital[13].write(1)
        time.sleep(delay)
        board.digital[13].write(0)
        time.sleep(delay)
        
try:
    number=int(input("enter number"))
    print(number)
except ValueError:
    print("There is a value error")      

  
blinkled(number)

def MoveMotor(direction,speed=0.5,duration=1):
    # Dir1 pin on mCore is D7
    board.digital[7].write(0)
    # Dir1 pin on mCore is D4
    board.digital[4].write(1)

    motor1_pwm = board.digital[5]
    motor1_pwm.mode = PWM
    motor2_pwm = board.digital[6]
    motor2_pwm.mode = PWM

    motor1_pwm.write(speed)
    motor2_pwm.write(speed)
    time.sleep(duration)
    motor1_pwm.write(0)
    motor2_pwm.write(0)
    
MoveMotor(100,0.70,100)