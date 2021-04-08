#3,2
#[2,1,1,0,1]

#1 1 0 0 1
#1 0 1 0 0
import numpy as np
def solution(U, L, C):
    if sum(C) != U + L:
        return "IMPOSSIBLE"
    else:
        urow=[]
        lrow=[]
        #uidx=0
        #lidx=0
        idx=0
        urow_cnt=U
        lrow_cnt=L
        for i in C:
            if i == 2:
                #urow[idx]=1
                #lrow[idx]=1
                urow.append(1)
                lrow.append(1)
                urow_cnt-=1
                lrow_cnt -= 1
            elif i == 0:
                #urow[idx]=0
                #lrow[idx]=0
                urow.append(0)
                lrow.append(0)
            elif i == 1:
                if urow_cnt >=1:
                    #urow[idx] = 1
                    #lrow[idx] = 0
                    urow.append(1)
                    lrow.append(0)
                    urow_cnt -= 1
                else:
                    #urow[idx] = 0
                    #lrow[idx] = 1
                    urow.append(0)
                    lrow.append(1)
                    lrow_cnt -= 1
    if sum(urow) == U and sum(lrow) == L:
        a=''.join(map(str, urow))
        b = ''.join(map(str, lrow))
        return str(int(a))+","+str(int(b))
#print(solution(3,2,[2,1,1,0,1]))
#print(solution(2,3,[0,0,1,1,2]))
print(solution(2,2,[2,0,2,0]))