from pyfirmata import util
import time


SET_TONE = 0x74


def play_sound(board, duration = 400, frequency = 200):
    
    board.send_sysex(SET_TONE, util.to_two_bytes(duration)+util.to_two_bytes(frequency) ) 
    
def blinkled(board, count, delay=0.2):
    for x in range(count):
        board.digital[13].write(1)
        time.sleep(delay)
        board.digital[13].write(0)
        time.sleep(delay)
