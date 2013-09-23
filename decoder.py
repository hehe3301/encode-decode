'''
filename:    decoder.py
language:    Python3
description: This file decodes a message by turning the tring of numbers into a message
author:      Alex Habermann hehe3301@gmail.com
created:     2013-09-22
edited:      2013-09-22 by Alex Habermann
'''

from numswap import *

#message=list((input('What mesage would you like to decode? ')))
encoded=list([48, 18, 114, 100, 75, 126, 266, 152, 45, 240, 275, 456, 26, 70, 15, 304, 340]) # Temp solution paste here
code=list()
message=list()

for q in range (0,len(encoded)):
    code.append( encoded[q]/(q+1) )
    q=q+1


for i in range (0,len(code)):
    message.append((numberswap(code[i])))
    i=i+1
  
print(message)
