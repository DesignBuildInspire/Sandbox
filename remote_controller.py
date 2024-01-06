import serial.tools.list_ports
from pyfirmata import Arduino, util, Board, SERVO, PWM
from pyfirmata.boards import BOARDS
import time
from pynput import keyboard
from pynput.keyboard import Key

FORWARD = 0
BACKWARD = 1
LEFT = 2
RIGHT =3

def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))

mbot = Arduino(get_mbot_port(),baudrate=115200)

iterator = util.Iterator(mbot)
iterator.start()

def on_key_release(key):
    if key == Key.right:
        print("Right key clicked")
        MoveMotor(RIGHT, 0.5,1)

    elif key == Key.left:
        print("Left key clicked")
        MoveMotor(LEFT, 0.5,1)

    elif key == Key.up:
        print("Up key clicked")
        MoveMotor(FORWARD, 0.5,1)

    elif key == Key.down:
        print("Down key clicked")
        MoveMotor(BACKWARD, 0.5,1)

    elif key == Key.esc:
        exit()

def MoveMotor(direction,speed=0.5,duration=1):
    
    if(direction==FORWARD):
        mbot.digital[7].write(0)
        mbot.digital[4].write(1)
    elif(direction==BACKWARD):
        mbot.digital[7].write(1)
        mbot.digital[4].write(0)
    elif(direction==LEFT):
        mbot.digital[7].write(1)
        mbot.digital[4].write(1)
    elif(direction==RIGHT):
        mbot.digital[7].write(0)
        mbot.digital[4].write(0)
    else:
        print("wrong direction")

    motor1_pwm = mbot.digital[5]
    motor1_pwm.mode = PWM
    motor2_pwm = mbot.digital[6]
    motor2_pwm.mode = PWM

    motor1_pwm.write(speed)
    motor2_pwm.write(speed)
    time.sleep(duration)
    motor1_pwm.write(0)
    motor2_pwm.write(0)

MoveMotor(FORWARD, 0.5,1)
    





with keyboard.Listener(on_release=on_key_release) as listener:
    listener.join()
    
