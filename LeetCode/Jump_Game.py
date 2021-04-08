arr=[1,3,2,0,2]
#arr=[1,1,2,5,2,1,0,0,2,2,3]
#arr=[1,1,2,3,2,1,0,0,2,2,3]
reachable=0
flag=False
for idx,i in enumerate(arr):
    if arr[idx] !=0 :
        print(idx,i,reachable)
        if reachable < idx:
            flag=False
            break
        if arr[idx + i] != 0:
            reachable=max(reachable,idx+i)
        #else:
        #    flag=False
        #    break
        if reachable == len(arr)-1:
            print("Reachable:",reachable)
            flag=True
            break
if flag:
    print("yes")
else:
    print("No..")
