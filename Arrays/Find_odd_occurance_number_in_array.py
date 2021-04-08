def findby_map(arr):
    map={}
    for i in arr:
        if i in map:
            j=map[i]+1
            map[i]=j
        else:
            map[i]=1
    num=[k for k,v in map.items() if v%2 !=0 ]
    return num
def findby_xor(arr):
    result=arr[0]
    for i in arr[1:]:
        result=result ^ i
        #print(i)
    return result
arr1=[2,5,9,1,5,1,8,2,8]
print(findby_map(arr1))
print(findby_xor(arr1))
