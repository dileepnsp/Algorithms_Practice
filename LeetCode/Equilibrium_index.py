arr=[-7,1,5,2,-4,3,0]
#Approach 1 -> Brute Force.

for idx,i in enumerate(arr):
    if idx == 0:
        continue
    if idx == len(arr)-1:
        print("No equilibrium..")
    else:
        #print(arr[idx])
        #print("Left side sum:",sum(arr[0:idx]))
        #print("Right side sum:",sum(arr[idx+1:]))
        if sum(arr[0:idx]) == sum(arr[idx+1:]):
            print(arr[idx])
            break

#Approach 2:
