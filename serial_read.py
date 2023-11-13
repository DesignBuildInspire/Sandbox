import serial
import time

serialComm = serial.Serial("/dev/tty.usbserial-1420",115200)
serialComm.timeout = 1

while True:
    i = input("input:").strip()
    if i == 'done':
        print("exit")
        break
    time.sleep(0.5)
    print(serialComm.readline().decode('ascii'))

serialComm.close()

