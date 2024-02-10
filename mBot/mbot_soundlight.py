from pyfirmata import util
# from notes import *
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

def play_victory(board):
    melody = furelise()
    beat = 15
    
    for x in range(0,len(melody),2):

        if melody[x+1]>0:
            duration = beat * melody[x+1]
        else:
            duration = -1* int( beat*1.05 ) * melody[x+1]
        if melody[x]>0:
            frequency = melody[x]
        else:
            time.sleep(duration/1000)
            continue
        board.send_sysex(SET_TONE, util.to_two_bytes(duration)+util.to_two_bytes(frequency) )
        time.sleep(duration/1000)