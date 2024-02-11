from mBot.notes import *
from mBot.init import *
from mBot.mbot_motion import *
from mBot.mbot_soundlight import *
from mBot.mbot_sensors import *
from pynput import keyboard
from pynput.keyboard import Key

mbot= init_mbot()
initMotor(mbot)

def on_key_release(key):
    try:
        if key.char == 'd':
            move_arm(mbot , 11 , 80)
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
        if key.char == 'w':
            move_arm(mbot,12,0)
        if key.char == 'd':
            move_arm(mbot,12,120)
        if key.char == 'm':
            play_sound(mbot,500,NOTE_A5)
    except AttributeError:
        if key == Key.right:
            print("Right key press")
            startMove(mbot,RIGHT, 0.75)
        elif key == Key.left:
            print("Left key press")
            startMove(mbot,LEFT, 0.75)
        elif key == Key.up:
            print("Up key press")
            startMove(mbot,FORWARD, 0.75)
        elif key == Key.down:
            print("Down key press")
            startMove(mbot,BACKWARD, 0.75)

        elif key == Key.esc:
            exit()     


with keyboard.Listener(on_press = on_key_press , on_release = on_key_release) as listener:
    listener.join()
    
# with keyboard.Listener(on_release=on_key_release) as listener:
#     listener.join()