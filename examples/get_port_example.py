import serial.tools.list_ports

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


print(get_board_port())
