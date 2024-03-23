from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT, OUTPUT
from pyfirmata.boards import BOARDS
from pynput import keyboard
from pynput.keyboard import Key



import time, sys, threading
import serial.tools.list_ports, time


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


def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))

# instantiate and register the cmd handler

board = Arduino(get_mbot_port(),baudrate=115200)
iterator = util.Iterator(board)
iterator.start()

D_in = board.digital[23]
CS_o = board.digital[22]
Clk = board.digital[21]

D_in.mode = OUTPUT
CS_o.mode = OUTPUT
Clk.mode = OUTPUT

D_in.write(0)
CS_o.write(1)
Clk.write(0)

delay_t = 0.0001

def push_byte(byte):
    
    for bit in range(7, -1, -1):
        # Set Data  to the current bit in the byte        
        D_in.write((int) ((byte & (1 << bit)) != 0))
        #print((int) ((byte & (1 << bit)) != 0))
        # # Toggle the clock
        Clk.write(1)
        time.sleep(delay_t)  # Adjust the delay as needed
        Clk.write(0)
        time.sleep(delay_t)  # Adjust the delay as needed


def setCommand(register, data):
    time.sleep(0.001) 
    CS_o.write(0)
    time.sleep(0.001) 
    push_byte(register)
    time.sleep(0.001) 
    push_byte(data)
    time.sleep(0.001) 
    CS_o.write(1)
    time.sleep(0.01) 

def setCommand_2x(register, data1, data2):
    CS_o.write(1)
    time.sleep(0.001) 
    CS_o.write(0)
    time.sleep(0.001) 
    push_byte(register)
    time.sleep(0.001) 
    push_byte(data1)
    time.sleep(0.001) 
    push_byte(register)
    time.sleep(0.001) 
    push_byte(data2)
    time.sleep(0.001) 
    CS_o.write(1)
    time.sleep(0.01) 
    



# Byte to transmit
# data_byte = 0x0CFF  # Replace with the actual byte you want to transmit
data_byte = 0x0A01  # Replace with the actual byte you want to transmit


# Transmit the byte over SPI
setCommand(max7219_reg_scanLimit, 0x07)   
time.sleep(0.01)   
setCommand(max7219_reg_decodeMode, 0x00)
time.sleep(0.01)   
setCommand(max7219_reg_shutdown, 0x01)
time.sleep(0.01)   
setCommand(max7219_reg_displayTest, 0x00)
time.sleep(0.01)   
setCommand(max7219_reg_intensity, 0x05)
time.sleep(0.01)   

for i in range(0,8):
    setCommand(i+1,0)
    
    
data = [0,0,0,16,0,0,0,0]


def display_screen(data):
    for i in range (0,8):
        setCommand(i+1,data[i])


display_screen(data)


def on_key_press(key):
    try:
        if key.char == 'd':
            return
    except AttributeError:
        if key == Key.right:
            print("Right key press")
        elif key == Key.left:
            print("Left key press")
        elif key == Key.up:
            print("Up key press")
        elif key == Key.down:
            print("Down key press")

        elif key == Key.esc:
            exit()     


with keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()