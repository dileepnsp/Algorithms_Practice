arr=[-1,0,1,2,-1,-4]
arr=sorted(arr)
print(arr)
result=[]
for idx,i in enumerate(arr):
    a=arr[idx]
    left_idx=idx+1
    right_idx=len(arr)-1
    while left_idx < right_idx and right_idx - left_idx >1:
        if arr[left_idx] + arr[right_idx] + a < 0:
            left_idx+=1
        if arr[left_idx] + arr[right_idx] + a > 0:
            right_idx -= 1
        if arr[left_idx] + arr[right_idx] + a == 0:
            result.append([a,arr[left_idx],arr[right_idx]])
            break
        #print("left idx:",left_idx,"right idx:",right_idx)

print(result)
