from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT
from pyfirmata.boards import BOARDS

import time

def main():
    board = Arduino("/dev/tty.usbserial-1440",baudrate=115200)
    
    sensor_left = board.digital[9]
    sensor_right = board.digital[10]
    
    sensor_left.mode = INPUT
    sensor_right.mode = INPUT
    
    iterator = util.Iterator(board)
    iterator.start()
    
    time.sleep(.1)
    

    
    while True:
        data=sensor_left.read()
        if data is not None:
            print(data)
            break
        else:
            print(data)

    
    print(sensor_right.read())


    
    
    


    

    
if __name__ == "__main__":
    main()