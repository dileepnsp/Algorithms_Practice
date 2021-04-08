import numpy as np
arr=np.array([2,4,7,1,5,3])
min=-1
for i in range(0,len(arr)):
    for j in range(i,len(arr)-1):
        if arr[j] < arr[j+1]:
            min=j
    temp=arr[i]
    arr[i]=arr[min]
    arr[min]=temp
print(arr)

