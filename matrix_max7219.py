from pyfirmata import Arduino, util, Board, SERVO
from pyfirmata import PWM, ANALOG, I2C_REQUEST, INPUT, OUTPUT
from pyfirmata.boards import BOARDS

import time, sys, threading
import serial.tools.list_ports, time




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

def spi_write_byte(byte):
    
    CS_o.write(0)
    time.sleep(0.01)
    
    for bit in range(15, -1, -1):
        # Set Data  to the current bit in the byte        
        D_in.write((int) ((byte & (1 << bit)) != 0))
        print((int) ((byte & (1 << bit)) != 0))
        # # Toggle the clock
        Clk.write(1)
        time.sleep(0.01)  # Adjust the delay as needed
        Clk.write(0)

    # Deselect the slave (SS)
    CS_o.write(1)



# Byte to transmit
# data_byte = 0x0CFF  # Replace with the actual byte you want to transmit
data_byte = 0x0A01  # Replace with the actual byte you want to transmit


# Transmit the byte over SPI
spi_write_byte(data_byte)