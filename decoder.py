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
encoded=list([114, 117, 99, 98, 97, 114]) # Temp solution paste here
code=list()
message=''

for q in range (len(encoded)):
    code.append( encoded[q] )
    


for i in range (len(code)):
    message=message+chr(code[i])
    
print(message)
