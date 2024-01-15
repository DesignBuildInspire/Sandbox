import time
from pyfirmata import PWM, SERVO

FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT =3

def moveMotor(board, direction,speed=0.5,duration=1):
    
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
    
def move_arm(board,pin=11, angle=90):
    servo = board.digital[pin] # can be 11 or 12 , we can try both.
    servo.mode = SERVO
    servo.write(angle)