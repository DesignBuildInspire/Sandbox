import time
from pyfirmata import util, OUTPUT

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


def init_LED(board): 
    CS_out = board.digital[14]
    CS_out.mode = OUTPUT
    CS_out.write(1)
    return CS_out


def push_Byte(board, data):
    board.send_sysex(SET_SPI, util.to_two_bytes(data))


def setCommand(board, register, data,CS_out):
    CS_out.write(0)
    push_Byte(board,register)
    push_Byte(board,data)
    CS_out.write(1)
    

def setCommand_2(board, register, data1, data2,CS_out):
    CS_out.write(0)
    push_Byte(board,register)
    push_Byte(board,data1)
    push_Byte(board,register)
    push_Byte(board,data2)
    CS_out.write(1)