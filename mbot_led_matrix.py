from pyfirmata import Arduino, util, Board, SERVO, OUTPUT
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS
import serial.tools.list_ports
from mBot.notes import *

import time

PING_READ = 0x75
SET_TONE = 0x74
SET_SPI = 0x73


def get_board_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            # print("name= " + str(p.name))
            # print("description= " + str(p.description))
            # print("location= " + str(p.location))
            # print("device= " + str(p.device))
            # print("interface= " + str(p.interface))
            # print("product= " + str(p.product))
            return(str(p.device))

# instantiate and register the cmd handler
board = Arduino(get_board_port(),baudrate=115200)

iterator = util.Iterator(board)
iterator.start()

duration = 100
frequency = 200

melody_1= (REST, 2, NOTE_D4, 4, NOTE_G4, -4, NOTE_AS4, 8, NOTE_A4, 4, NOTE_G4, 2, NOTE_D5, 4)
melody_2= ( NOTE_CS4, 2, NOTE_AS4, 4)

beat = 25

def Play_melody(melody,beat):
    for i in range(0,len(melody),2):
        frequency = melody_1[i]
        duration = beat * abs(melody[i+1])
        if (frequency != REST):
            board.send_sysex(SET_TONE, util.to_two_bytes(duration)+util.to_two_bytes(frequency) )
        time.sleep(duration/1000)


board.digital[14].mode = OUTPUT

board.digital[14].write(1)

def push_Byte(board, data):
    board.send_sysex(SET_SPI, util.to_two_bytes(data))



Play_melody(melody_1,beat)
time.sleep(.1)
board.digital[14].write(0)
push_Byte(board, 0x45)
push_Byte(board, 0x54)

board.digital[14].write(1)
