import threading
import time
from mBot.notes import *
from mBot.init import *
from mBot.mbot_motion import *
from mBot.mbot_soundlight import *
from mBot.mbot_sensors import *


mbot= init_mbot()
setup_line_sensor(mbot)


def task1():
    for _ in range(5):
        moveMotor (mbot, FORWARD, 0.5, 1)
        time.sleep(1)
        moveMotor (mbot, BACKWARD, 0.5, 1)
        time.sleep(1)       

def task2():
    for _ in range(20):
        print(read_line_sensor(mbot))
        time.sleep(.25)

# Create threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")