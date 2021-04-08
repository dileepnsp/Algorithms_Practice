import numpy as np
arr=np.array([1,4,10,5,18,7,9,11,14,17,19,20])
n=4
m=0
iter=arr.size-n
lst=[]
print(iter)
for i in range(iter+1):
    print(i)
    lst.append(max(arr[i:n+i]))
print(lst)

