def binarySearch(array, target):
    left=0
    right=len(array)-1
    while left <= right:
        print(left,right)
        mid=int((left+right)/2)
        print("mid:",mid)
        if target > array[mid]:
            left=mid+1
        if target < array[mid]:
            right=mid-1
        if target == array[mid]:
            return mid
    return -1
print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73],33))
#print(binarySearch([1, 5, 23, 111],111))