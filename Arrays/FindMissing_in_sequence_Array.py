import numpy as np
arr=np.array([1,2,3,5,6,7])
low=0
high=len(arr)-1
mid=0
while low <=high:
    mid=(low+high)//2
    print("mid:",mid)
    print("low:",low)
    print("high:",high)
    if mid == arr[mid]-1 :
        low=mid+1
    else:
        high=mid-1
#if (low == len(arr)-1 or high == len(arr)-1) and :
if mid == arr[mid]-1:
    print("No missing")
else:
    print("missing element is:",arr[low]-1)
