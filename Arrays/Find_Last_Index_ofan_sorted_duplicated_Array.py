#Time complexity : o(logn)
#Space complexity : o(1)
import numpy as np
import sys
arr=np.array([0, 1, 2, 2, 4, 5, 5, 5, 8])
print(arr)
find_element=5
start=0
end=arr.__len__()-1
while start <= end:
    mid=(start+end)//2
    #print(start)
    #print(end)
    #print(mid)
    if find_element < arr[mid]:
        end=mid-1
    else:
        if find_element > arr[mid]:
            start=mid+1
        else:
            if find_element == arr[mid]:
                if mid == end :
                    print(mid)
                    sys.exit(0)
                elif arr[mid+1] == find_element:
                    print(mid+1)
                    sys.exit(0)
