from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT
from pyfirmata.boards import BOARDS
import time

FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT =3

board = Arduino("/dev/tty.usbserial-1430",baudrate=115200)

sensor_left = board.digital[9]
sensor_right = board.digital[10]

sensor_left.mode = INPUT
sensor_right.mode = INPUT

iterator = util.Iterator(board)
iterator.start()

time.sleep(.1)

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

# try:
#     number=int(input("enter number"))
#     print(number)
# except ValueError:
#     print("There is a value error")    

# MoveMotor(1,0.70,number)

def get_position():
    left = int(sensor_right.read()) * 1
    right = int(sensor_left.read()) * 2

    return (left + right)

while True:
    if get_position() == 0 :
        MoveMotor(FORWARD, 0.5, 0.1)
    elif get_position() == 1:
        MoveMotor(LEFT, 0.5, 0.1)   
    elif get_position() == 2:
        MoveMotor(RIGHT, 0.5, 0.1)
    elif get_position() == 3:
        MoveMotor(BACKWARD, 0.5, 0.1) 