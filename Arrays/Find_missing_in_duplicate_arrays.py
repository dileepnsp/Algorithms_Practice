ar1=[9,7,8,5,4,6,2,3,1]
ar2=[2,4,3,9,1,8,5,6,7]
def find_dupl(arr1,arr2):
    result=arr1[0]
    for i in arr1[1:]:
        result=result ^ i
    for j in arr2:
        result=result ^ j
    return result
print(find_dupl(ar1,ar2))

