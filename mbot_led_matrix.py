from pyfirmata import Arduino, util, Board, SERVO, OUTPUT
from pyfirmata import PWM, ANALOG, I2C_REQUEST
from pyfirmata.boards import BOARDS
import serial.tools.list_ports
from mBot.notes import *

import time

PING_READ = 0x75
SET_TONE = 0x74
SET_SPI = 0x73

max7219_reg_noop        = 0x00
max7219_reg_digit0      = 0x01
max7219_reg_digit1      = 0x02
max7219_reg_digit2      = 0x03
max7219_reg_digit3      = 0x04
max7219_reg_digit4      = 0x05
max7219_reg_digit5      = 0x06
max7219_reg_digit6      = 0x07
max7219_reg_digit7      = 0x08
max7219_reg_decodeMode  = 0x09
max7219_reg_intensity   = 0x0a
max7219_reg_scanLimit   = 0x0b
max7219_reg_shutdown    = 0x0c
max7219_reg_displayTest = 0x0f



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

CS_out = board.digital[14]
CS_out.mode = OUTPUT
CS_out.write(1)


def push_Byte(data):
    global board
    board.send_sysex(SET_SPI, util.to_two_bytes(data))

def setCommand(register, data):
    global board
    CS_out.write(0)
    push_Byte(register)
    push_Byte(data)
    

def setCommand_2(register, data1, data2):
    global board
    CS_out.write(0)
    push_Byte(register)
    push_Byte(data1)
    push_Byte(register)
    push_Byte(data2)
    CS_out.write(1)

    

Play_melody(melody_1,beat)
time.sleep(.1)


# CS_out.write(1)

# Transmit the byte over SPI
setCommand_2(max7219_reg_scanLimit, 0x07, 0x07)   
time.sleep(0.1)   
setCommand_2(max7219_reg_decodeMode, 0x00, 0x00)
time.sleep(0.1)   
setCommand_2(max7219_reg_shutdown, 0x01, 0x01)
time.sleep(0.1)   
setCommand_2(max7219_reg_displayTest, 0x00, 0x00)
time.sleep(0.1)   
setCommand_2(max7219_reg_intensity, 0x01, 0x01)
time.sleep(0.1)   

for i in range(1,9):
    setCommand_2(i,0,0)

setCommand_2(1,1,1)


# dot = 0b00000011 
# for i in range(1,7):
#     dot = dot * 2
#     setCommand(1,0b00000000)
#     setCommand(2,0b00000000)
#     setCommand(3,0b00000000)
#     setCommand(4,dot)
#     setCommand(5,dot)
#     setCommand(6,0b00000000)   
#     setCommand(7,0b00000000)
#     setCommand(8,0b00000000)
#     time.sleep(0.5)