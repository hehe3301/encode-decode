from numswap import *
message=list(input('What mesage would you like to encode?'))
code=list()
i=0
for i in range (0,len(message)):
    code.append(letterswap(message[i]))
    i=i+1

print(message)
print(code)

