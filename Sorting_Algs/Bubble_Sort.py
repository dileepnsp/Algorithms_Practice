import numpy as np
arr=np.array([2,4,7,1,5,3])
#print(sorted(arr))
for j in range(0,len(arr)-1):
    for i in range(0,len(arr)-1-j):
        if arr[i] > arr[i+1]:
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
print(arr)