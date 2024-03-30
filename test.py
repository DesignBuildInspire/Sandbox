data = [0,0,0,16,0,0,0,0]

        
def list_x2(data):
    out=[]
    for i in range(len(data)):
        out.append(int(data[i]*2))
    return out

def list_dev2(data):
    out=[]
    for i in range(len(data)):
        out.append(int(data[i]/2))
    return out

def move_right(data):
    out=data
    out.insert(0,0)
    return out[0:8]

def move_left(data):
    out=data
    out.extend([0])
    return out[1:9]

print(data)
print (list_x2(data))
print (list_dev2(data))
# print (move_right(data))
print (move_left(data))