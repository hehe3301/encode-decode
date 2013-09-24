'''
filename:    encoder.py
language:    Python3
description: This file encodes a message by turning it into a string of numbers associated with each letter
author:      Alex Habermann hehe3301@gmail.com
created:     2013-09-22
edited:      2013-09-22 by Alex Habermann
'''
from numswap import *
import math
msg=list(input('What mesage would you like to encode? '))
pwd=list(input('With what passkey '))
code=list()
key=list()
encoded=list()
msglen=len(msg)
edge=math.floor(math.sqrt(msglen))+1
count=0
matrix=[]
mkey=[]
for i in range (0,len(msg)):
    code.append(ord(msg[i]))
    
for i in range (0,len(pwd)):
    key.append(ord(pwd[i]))

for q in range (0,len(code)):
    encoded.append( int(code[q]) )

for x in range(edge):
    tmp=[]
    for y in range(edge):
        if count < msglen:
            tmp.append(code[count])
        else:
            tmp.append(ord('.'))
        count=count+1
    matrix.append(tmp)
count=0
for x in range(edge):
    tmp=[]
    for y in range(edge):
        tmp.append(key[count % len(key)])
        count=count+1
    mkey.append(tmp)
    
def zero(m,n):
    '''
    makes a blank matrix
    '''
    new_matrix =[[0 for row in range(n)] for col in range(m)]
    return new_matrix

def mult(matrix1,matrix2):
    '''
    multiply matrices
    '''
    if len(matrix1[0]) != len(matrix2):
        #check matrix dim
        print('somthing borked')
    else:
        #multiply
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix

def prettyPrint(matrix):
    for row in matrix:
        print(row)

ans=mult(matrix,matrix)
#print(msg)
#print(code)
#print(key)
prettyPrint(mkey)

input('Hit enter to continue')

