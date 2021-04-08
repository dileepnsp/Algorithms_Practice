def isValidSubsequence(array, sequence):
    arr_ind=0
    seq_ind=0
    cnt=0
    while arr_ind != len(array) and seq_ind!=len(sequence):
        print("arr_ind:",arr_ind)
        print("seq_ind:",seq_ind)
        if array[arr_ind ]== sequence[seq_ind]:
            arr_ind=arr_ind+1
            seq_ind=seq_ind+1
            cnt=cnt+1
        else:
            arr_ind = arr_ind + 1
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