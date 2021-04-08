import numpy as np
arr=[[23, 34, 67, 89, 123, 566, 1000],
     [1, 22, 23, 24,33, 37, 185, 566, 987, 1223, 1234],
     [23, 43, 67, 98, 566, 678],
     [1, 4, 5, 23, 34, 76, 87, 132, 566, 665],
     [1, 2, 3, 23, 24, 344, 566]]
arrlen=len(arr)
print("array length:",arrlen)
## Find shortest array
short=100
for i in arr:
    if len(i) < short:
        short=len(i)
print("short array is:",short)
def binarysearch(low,high,element,eacharr):
    eacharr_index=range(0,len(eacharr))
    low=0
    high=len(eacharr)-1
    print(eacharr)
    while low <=high:
        mid=(low+high)//2
        print("mid:", mid)
        #print("element:",element,"eacharr[mid]",eacharr[mid])
        if element < eacharr[mid]:
            high=mid-1
            continue
        if element > eacharr[mid]:
            low = mid+1
            continue
        if element == eacharr[mid]:
            return mid
        else:
            return -1
    return -1
index_arry=[0,0,0,0]
common_elements=[]
for i in range(0,len(arr[0])):
    element=arr[0][i]
    print("element:",element)
    if short in index_arry:
        print("Traverse done")
        print(common_elements)
        break
    cnt=0
    for eacharr in range(1,arrlen):
        print("each arr:", eacharr)
        low=index_arry[eacharr-1]
        #print("low",low)
        #print("high:",len(arr[eacharr]))
        print("elelemnt:",element)
        value=binarysearch(index_arry[eacharr-1],len(arr[eacharr]),element,arr[eacharr])
        print("value:",value)
        if value != -1:
            print(element,"found in",arr[eacharr])
            index_arry[eacharr - 1]=value
            print(index_arry)
            cnt=cnt+1
    if cnt == arrlen-1:
        print("found:",element)
        common_elements.append(element)
print(common_elements)