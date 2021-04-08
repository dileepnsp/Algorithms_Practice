import numpy as np
arr=np.array([11,-8,16,-7,24,-2,3])
sum=0
sum_index=0
k=3
max_sum=0
max_index=0
for i in range(len(arr)-k+1):
    if i == 0:
        sum=arr[i]+arr[i+1]+arr[i+2]
        max_sum=sum
        max_index=i
    else:
        sum=sum+arr[i+2]-arr[i-1]
        if sum > max_sum:
            max_sum=sum
            max_index=i

print("max sum is:",max_sum)
print("max sum index is :",max_index+1)