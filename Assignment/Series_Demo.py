import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy import inexact

s=pd.Series(['dileep','likith','madhu','lohi'],index=['1','2','3','4'])
print(s)
print(s['1'])
print(s[1:3])
print('5' in s)
print(s.get('5',default='fuck'))
data = [[1,2013,'ar00001','Thailand',157500],
       [2,2014,'ar00002','Russia',458226],
       [3,np.NaN,'ar00003','South Korea',np.NaN],
       [4,2010,'ar00004',np.NaN,456312],
     [5,2018,'ar00005','England',235485]]

df = pd.DataFrame(data,columns=['Sr_No','Year','ID','Country','Sales'])
#print(df.Sr_No.head())
print(df[['Sr_No','Year']].head())
print(df.iloc[1:3].head())
df['newcol']=df['Sr_No'] > 5
print(df.head())
df1=df.pop('Year')
print(df1.head())
print(df.head())
df['Sr_No']='foo'
print(df.head())
#df.insert(1,'newcol',[11,2,55,44,22])
#df.insert(1,'newcol',df['Sr_No'])
newcol=pd.Series([11,2,44,33,22],index=[0,1,2,3,4])
df.insert(1, 'bar', newcol)
df.insert(1, 'mul', df['Sales']*3 )
print(df.head())
#newass=df.assign(newassign=df['mul'] / 10)
newass=df.assign(newassign = lambda x: (x['mul']/10))
print(newass.head())
print(newass.info())
newass['Sales']=newass['Sales'].fillna(0)
print(newass.head())
#asb=df.query('bar > 25')
#asb=df.query('Country == "Thailand"  or Country == "Russia"')
#print(asb)
#sff=df[(df['Country'] == "Thailand") | (df['Country'] == "Russia")]
#sff=df[(df['Country'] == "Thailand") & (df['bar'] == 2)]
#print(sff.head())
#sff.info()

newass.plot(kind='scatter', x='Sales', y='bar')
plt.show()
#gfg = pd.Series([10, 9.9, 9.8, 7.8, 6.7, 19, 5.5])
##gfg.plot()
#plt.show()
