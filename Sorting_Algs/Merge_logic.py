import numpy as np
arr1=np.array([3,6,8,9])
arr2=np.array([4,5,7,10])
i=0
j=0
k=0
final_arr=np.array([0,0,0,0,0,0,0,0])
while i <len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        final_arr[k]=arr1[i]
        i=i+1
    else:
        final_arr[k]=arr2[j]
        j=j+1
    k=k+1
print(i,j,k,final_arr)
while i < len(arr1):
    final_arr[k]=arr1[i]
    i=i+1
    k=k+1
while j < len(arr2):
    final_arr[k]=arr2[j]
    j=j+1
    k=k+1

print(i,j)
print(final_arr)