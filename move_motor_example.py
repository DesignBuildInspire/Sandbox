from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS

import time

FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT =3


board = Arduino("/dev/tty.usbserial-1430",baudrate=115200)

iterator = util.Iterator(board)
iterator.start()

def MoveMotor(direction,speed=0.5,duration=1):
    
    if(direction==FORWARD):
        board.digital[7].write(0)
        board.digital[4].write(1)
    elif(direction==BACKWARD):
        board.digital[7].write(1)
        board.digital[4].write(0)
    elif(direction==LEFT):
        board.digital[7].write(1)
        board.digital[4].write(1)
    elif(direction==RIGHT):
        board.digital[7].write(0)
        board.digital[4].write(0)
    else:
        print("wrong direction")

    motor1_pwm = board.digital[5]
    motor1_pwm.mode = PWM
    motor2_pwm = board.digital[6]
    motor2_pwm.mode = PWM

    motor1_pwm.write(speed)
    motor2_pwm.write(speed)
    time.sleep(duration)
    motor1_pwm.write(0)
    motor2_pwm.write(0)
    
    
try:
    number=int(input("enter number"))
    print(number)
except ValueError:
    print("There is a value error")    

MoveMotor(1,0.70,number)



