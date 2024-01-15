import serial.tools.list_ports, time
from pyfirmata import Arduino, util, SERVO, PWM
from pyfirmata.boards import BOARDS


def get_mbot_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if '1A86:7523' in str(p.hwid):
            return(str(p.device))


def init_mbot():
    mbot = Arduino(get_mbot_port(),baudrate=115200)
    iterator = util.Iterator(mbot)
    iterator.start()
    time.sleep(.1)
    return mbot