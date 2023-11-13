from pyfirmata import Arduino, util, Board
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS

import time

PING_READ = 0x75

class myBoard(Board):
    """
    A board that will set itself up as a normal Arduino.
    """
    def __init__(self, *args, **kwargs):
        self.distance = 0
        args = list(args)
        args.append(BOARDS['arduino'])
        super().__init__(*args, **kwargs)
        
    def _handle_ping(self, *data):
        self.distance = data[2] << 7 | data[0]
        # print(distance)
        # do your thing


board = myBoard("/dev/tty.usbserial-1410",baudrate=115200)

board.add_cmd_handler(PING_READ, board._handle_ping)

iterator = util.Iterator(board)
iterator.start()

while True: 
    board.send_sysex(PING_READ, bytes([0xff]) ) 
    print(board.distance)
    time.sleep(.1)
