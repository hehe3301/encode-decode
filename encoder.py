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

