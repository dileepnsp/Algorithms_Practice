'''import re
str="hello dileep.age is 34"
#pattern='\D+'
#pattern='\w+'
pattern='^h...4$'
ptrns=re.findall(pattern,str)
print(ptrns)
print("hello")
'''
import numpy as np

arr=np.array([[1,2],[3,4]])
print(arr)
print(arr.shape)
print(arr.size)
print(arr.ndim)

nar=np.empty(shape=[2,3],dtype=int)
print(nar)
nz=np.zeros(shape=[3,3],dtype=float,order='C')
print(nz)
nz=np.zeros(shape=[3,3],dtype=float,order='F')
print(nz)
none=np.ones(shape=[4,3],dtype=int,order='F')
print(none)
row1=np.empty(shape=[1,3],dtype=int)
row2=np.zeros(shape=[1,3],dtype=int)
row3=np.ones(shape=[1,3],dtype=int)
print(row1)
print(row2)
print(row3)
assignarra=np.array([row1,row2,row3])
#assignarra=np.array(row1,row2,row3)
print(assignarra)
print(np.linspace(1,10))
