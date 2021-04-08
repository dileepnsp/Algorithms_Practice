def isValidSubsequence(array, sequence):
    arr_ind=0
    cnt=0
    #print(sequence)
    for i in range(0,len(sequence)):
        for j in range(arr_ind,len(array)):
            if sequence[i] == array[j]:
                print("match:",i,j)
                arr_ind=j+1
                seq_ind=i+1
                cnt=cnt+1
                break
    print("cnt:",cnt)
    if cnt == len(sequence):
        return True
    else:
        return False
#print(isValidSubsequence([1,2,3,4],[1,3,4]))
#print(isValidSubsequence([1,2,3,4],[2,4]))
#print(isValidSubsequence([1, 1, 1, 1, 1],[1,1]))
#print(isValidSubsequence([1,2,3,4],[2,6]))
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, 22, 22, 25, 6, -1, 8, 10]))