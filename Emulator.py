# QT4001 emulator
import os
#thanks reddit for this code
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions
fn = askopenfilename()
file = open(fn,"r") # opens a file

#this returns each line as an item in a list
with open(fn) as file:
    listfile = file.readlines()

#were getting what we can actually use
actual_data = []
for line in listfile:
    if str(line[0]+line[1]) == "//":
        pass
    else:
        if line[0].isnumeric():
            if int(line[0]) not in range(0,9):
                print("invalid character code 1")
                exit()
            else:
                actual_data.append(line)
        else:
           print("invalid character code 2")
           exit()

# now we organise it
data = []
for item in actual_data:
    d = item.split()
    for thing in d:
        try:
            data.append(int(thing))
        except:
            print('bro you got another invalid character')
            exit()

# now lets check if they put in the right amount of bytes
if len(data) not in range(0,15):
    print("Bro you put in the wrong amount of shit")
    exit()
#set up the top row
R = 0
IS = 0
IP = 1 # which cell it stopped at / is executing
steps = 1

#remember to use hex!

Cells = [0,0,0,0,
         0,0,0,0,
         0,0,0,0,
         0,0,0,0
         ]

Cells = data
#Now we gotta do hexadecimal stuff

#And we should also do loop arounds
def looparound(x):
    if x >= 16:
        x = x - 16
    return x

#stuff for all the instructions
for thing in Cells:
    if thing == 0:
        print("halted")
        break
    elif thing == 1:
        R +=1
        R = looparound(R)
    elif thing == 2:
        R +=2
        R = looparound(R)
    elif thing == 3:
        R +=4
        R = looparound(R)
    elif thing == 4:
        R +=8
        R = looparound(R)
    elif thing == 7:
        print("Bell ring frfr")
    elif thing == 8:
        print(R) #but in decimal
    elif thing == 9:
        print(hex(R)    ) #but in hex
    else:
        print("invalid value")
        break
    IP +=1
    IS = thing
    steps +=1

#convert the list to hex
HexCells = []
for thing in Cells:
    h = str(hex(thing))
    h = h.replace("0x",'')
    HexCells.append(h)
print("IP: {}--- IS: {}--- R: {}".format(IP,IS,R))
print(HexCells)
print("{} steps taken".format(steps))
