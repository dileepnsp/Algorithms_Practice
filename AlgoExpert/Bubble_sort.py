a=[8,1,2,4,6,0,19]
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if a[i] > a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)