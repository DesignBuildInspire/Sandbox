from pyfirmata import Arduino, util, Board, SERVO, PWM
from pyfirmata import ANALOG, I2C_REQUEST, INPUT
from pyfirmata.boards import BOARDS
import time


mbot = Arduino("/dev/tty.usbserial-1430",baudrate=115200)

iterator = util.Iterator(mbot)
iterator.start()

motor1_pwm = mbot.digital[5]
motor1_pwm.mode = PWM


servo1 = mbot.digital[11]
servo1.mode = SERVO

servo2 = mbot.digital[12]
servo2.mode = SERVO

# this requires changing the Arduino dict board.py file in Pyfirmata to this 'digital': tuple(x for x in range(22)),
servo3 = mbot.digital[15]
servo3.mode = SERVO
servo3.write(90)


# servo3.write(180)
# time.sleep(4)
# servo3.write(50)
# time.sleep(1)
# servo3.write(90)

# servo1.write(90)
for i in range (0,120,10):
    time.sleep(0.04)
    servo1.write(i)

# servo2.write(90)
# time.sleep(1)
# servo2.write(0)

# time.sleep(1)
# servo1.write(90)


def MoveMotor(direction,speed,duration):
    # right motor direction . 0 means backwards // 1 means forward
    mbot.digital[4].write(direction)
    # this line sets the speed from 0 to 1 : 0 means Stop, 1 is fastest speed
    motor1_pwm.write(speed)
    # this line waits for the motor to move a number of seconds
    time.sleep(duration)
    # this line stops the Robot
    motor1_pwm.write(0)


    
# MoveMotor(1,1,2)

