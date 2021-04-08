import numpy as np
k=4
ip=np.array([9,6,11,8,10,5,14,13,93,14])
lst=[]
for j in range(len(ip)-k+1):
    for i in range(j,j+5):
        if len(lst) == 0:
            lst.append(i)
        else:
            lst_value=lst[len(lst) - 1]
            while len(lst) > 0 and ip[lst_value] < ip[i]:
                lst.pop()
                lst_value = lst[len(lst) - 1]
            lst.append(i)
    print(ip[lst[0]])