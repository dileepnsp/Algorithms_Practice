import numpy as np
import sys
arr=np.array([0, 1, 2, 2, 4, 5, 5, 5, 8])
print(arr)
find_element=5
start=0
end=arr.__len__()-1
while start <= end:
    mid=(start+end)//2
    if find_element < arr[mid]:
        end=mid-1
    elif find_element > arr[mid]:
        start=mid+1
    else:
        if find_element == arr[mid]:
            if arr[mid-1] == find_element:
                print(mid)
            elif mid == start:
                print(mid)
        print(mid)