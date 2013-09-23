'''
filename:    encoder.py
language:    Python3
description: This file encodes a message by turning it into a string of numbers associated with each letter
author:      Alex Habermann hehe3301@gmail.com
created:     2013-09-22
edited:      2013-09-22 by Alex Habermann
'''
from numswap import *

message=list(input('What mesage would you like to encode? '))
code=list()
encoded=list()
for i in range (0,len(message)):
    code.append(letterswap(message[i]))
    i=i+1

for q in range (0,len(code)):
    encoded.append( int(code[q])*(q+1) )
    q=q+1

print(message)
print(code)
print(encoded)

input('Hit enter to continue')

