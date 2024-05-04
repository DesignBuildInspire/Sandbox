from mBot.notes import *
from mBot.init import *
from mBot.mbot_motion import *
from mBot.mbot_soundlight import *
from mBot.mbot_sensors import *
from pynput import keyboard
from pynput.keyboard import Key
from mBot.ledMatrix import *

mbot= init_mbot()
initMotor(mbot)
init_LED(mbot)

# Transmit the byte over SPI
setCommand_2(mbot,max7219_reg_scanLimit, 0x07, 0x07)   
time.sleep(0.1)   
setCommand_2(mbot,max7219_reg_decodeMode, 0x00, 0x00)
time.sleep(0.1)   
setCommand_2(mbot,max7219_reg_shutdown, 0x01, 0x01)
time.sleep(0.1)   
setCommand_2(mbot,max7219_reg_displayTest, 0x00, 0x00)
time.sleep(0.1)   
setCommand_2(mbot,max7219_reg_intensity, 0x01, 0x01)
time.sleep(0.1)   

for i in range(1,9):
    setCommand_2(mbot,i,0,0)
    time.sleep(0.01)


def on_key_release(key):
    try:
        if key.char == 'd':
            move_arm(mbot,11,80)
        if key.char == 'u':
            move_arm(mbot,11,100)
    except AttributeError:
        if key == Key.right:
            print("Right key release")
            stopMove(mbot,RIGHT)
        elif key == Key.left:
            print("Left key release")
            stopMove(mbot,LEFT)
        elif key == Key.up:
            print("Up key release")
            stopMove(mbot,FORWARD)
        elif key == Key.down:
            print("Down key release")
            stopMove(mbot,BACKWARD)

        elif key == Key.esc:
            exit()

def on_key_press(key):
    try:
        if key.char == 'd':
            move_arm(mbot,11,80)
        if key.char == 'u':
            move_arm(mbot,11,100)
        if key.char == 'm':
            play_sound(mbot,500,NOTE_A5)
    except AttributeError:
        if key == Key.right:
            print("Right key press")
            startMove(mbot,RIGHT, 0.5)
        elif key == Key.left:
            print("Left key press")
            startMove(mbot,LEFT, 0.5)
        elif key == Key.up:
            print("Up key press")
            startMove(mbot,FORWARD, 0.5)
        elif key == Key.down:
            print("Down key press")
            startMove(mbot,BACKWARD, 0.5)

        elif key == Key.esc:
            exit()     


with keyboard.Listener(on_press=on_key_press,on_release=on_key_release) as listener:
    listener.join()
    
# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()