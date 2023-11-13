from pyfirmata import Arduino, util
from  pyfirmata import PWM, ANALOG
import time


board = Arduino("/dev/tty.usbserial-1430",baudrate=115200) 

iterator = util.Iterator(board)
iterator.start()

number = input("how many times do you want to flash ?")
number = int(number)

for x in range(1,number):
    board.digital[13].write(1)
    time.sleep(.25)

    board.digital[13].write(0)
    time.sleep(.25)