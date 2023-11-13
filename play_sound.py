from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS
import time

SET_TONE = 0x74

def main():
    board = Arduino("/dev/tty.usbserial-1430",baudrate=115200)

    iterator = util.Iterator(board)
    iterator.start()
    # buzzer_pin = 8
    
    board.send_sysex(SET_TONE, bytes([0xff]) ) 

    
    
    

    
if __name__ == "__main__":
    main()