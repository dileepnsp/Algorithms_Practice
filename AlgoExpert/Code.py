def solution(S, A):
    # write your code in Python 3.6
    str=S[0]
    k=0
    i=-1
    while i!=0:
        i=A[k]
        str=str+S[i]
        k = i
    return str[0:len(str)-1]

print(solution("cdeo",[3,2,0,1]))
#print(solution("cdeenetpi",[5,2,0,1,6,4,8,3,7]))
print(solution("bytdag",[4,3,0,1,2,5]))