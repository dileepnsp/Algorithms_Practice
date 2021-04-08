import numpy as np
#arr=np.array([2,4,1,6,8,5,3,7])
def merge_sort(arr):
    if len(arr) >1:
        mid=len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        merge_sort(l)
        merge_sort(r)
        print("After merge sort R")
        i = j = k = f=0
        final_length=len(l)+len(r)
        print(final_length)
        while i< len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k]=l[i]
                k=k+1
                i=i+1
            else:
                arr[k]=r[j]
                j=j+1
                k=k+1
        while i < len(l):
            arr[k]=l[i]
            k=k+1
            i=i+1
        while j < len(r):
            arr[k]=r[j]
            k=k+1
            j=j+1
arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
print(arr)
merge_sort(arr)
print(arr)
