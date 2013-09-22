'''
filename:    encoder.py
language:    Python3
description: This file encodes a message by turning it into a string of numbers associated with each letter
author:      Alex Habermann hehe3301@gmail.com
created:     2013-09-22
edited:      2013-09-22 by Alex Habermann
'''
from numswap import *
from numpy import matrix
from numpy import linalg
message=list(input('What mesage would you like to encode? '))
code=list()

for i in range (0,len(message)):
    code.append(letterswap(message[i]))
    i=i+1

print(message)
print(code)

input('Hit enter to continue')

