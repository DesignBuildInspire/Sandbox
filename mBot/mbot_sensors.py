from pyfirmata import INPUT
import time


def setup_line_sensor(board,pin_left=9, pin_right=10):
    board.digital[pin_left].mode = INPUT
    board.digital[pin_right].mode = INPUT
    
def read_line_sensor(board,pin_left=9, pin_right=10):
    while True:
        time.sleep(.1)
        data=board.digital[pin_left].read()
        if data is not None:
            left = int(data) * 1
            break
    while True: 
        time.sleep(.1)
        data=board.digital[pin_right].read()
        if data is not None:
            right = int(data) * 2
            break

    return (left + right)