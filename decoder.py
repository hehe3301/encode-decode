'''
filename:    decoder.py
language:    Python3
description: This file decodes a message by turning the tring of numbers into a message
author:      Alex Habermann hehe3301@gmail.com
created:     2013-09-22
edited:      2013-09-22 by Alex Habermann
'''

from numswap import *

message=(input('What mesage would you like to decode? '))
code=list()

for i in range (0,len(message)):
    code.append(numberswap(message[i]))
    i=i+1

print(message)
print(code)
