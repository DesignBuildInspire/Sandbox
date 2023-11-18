# This code takes name and prints hello world..
# name=input("enter your name")
# print("hello world: " + name) 

while True:
    try :
        number_1 = int(input ("enter first number"))
        break
    except ValueError:
        print("error")

while True:
    try :
        number_2 = int(input ("enter second number"))
        break
    except ValueError:
        print("error")



print(type(number_1))
print ("the Sum = ", number_1 + number_2)
print(type(number_1+number_2))