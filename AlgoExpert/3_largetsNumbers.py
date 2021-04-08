import numpy as np
def shiftarray(num,array,idx):
    for i in range(idx+1):
        if i == idx:
            array[i]=num
        else:
            array[i]=array[i+1]
    print(array)
def findThreeLargestNumbers(array):
    # Write your code here.
    op=[None,None,None]
    for i in array:
        if op[2] is None or i > op[2]:
            shiftarray(i,op,2)
        elif op[1] is None or i > op[1]:
            shiftarray(i,op,1)
        elif op[0] is None or i > op[0]:
            shiftarray(i,op,0)
    return op

#print(findThreeLargestNumbers([10,5,9,10,12]))
print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))

