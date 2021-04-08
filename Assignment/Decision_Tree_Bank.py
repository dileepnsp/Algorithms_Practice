import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
bank=pd.read_csv(r"C:\Users\cdileepkumar\Documents\02 Python_Practice\Python_Practice\bank-additional-full.csv",sep=";")
print(bank)
pd.set_option('display.max_columns',21)
print(bank.columns)
pd.reset_option('display.max_columns',21)
print(bank.columns)
labels=['yes','no']
sizes=[bank.y[bank['y']=='yes'].count(),bank.y[bank['y']=='no'].count()]
fig,ax=plt.subplots()
ax.pie(sizes,labels=labels,explode=(0.1,0),autopct='%1.1f%%',shadow=True,startangle=90,textprops={'fontsize':14})
plt.legend(loc='upper right')
plt.show()
print(bank.info())
# CHange object type to catergory type
for col in bank.select_dtypes("object"):
    bank[col]=bank[col].astype("category")
print(bank.info())
# Descripe
print(bank.describe())
#Check nulls
print(bank.isnull().sum())
#Outlier Analysis
sns.set()
fig = plt.figure(figsize=(19,17))
i = 1
for column in bank.select_dtypes(["int64","float64"]):
    plt.subplot(5,2,i)
    sns.boxplot(bank[column])
    i = i+1
plt.tight_layout()
plt.show()

#Univariate Analysis for Categorical Variables.
sns.set(rc={'figure.figsize':(24,24)}, font_scale=1.5)
i=1
for col in bank.select_dtypes(["category"]):
    if col != "y":
        plt.subplot(5,2,i)
        sns.countplot(bank[col])
        i=i+1
        plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


## Univariant analysis for continous variables
i=1
sns.set(rc={'figure.figsize':(24,24)}, font_scale=1.5)
#sns.distplot(bank['age'])
#plt.show()
#import sys
#sys.exit(0)
#for col in bank.select_dtypes(["int64","float64"]):
#    #plt.subplot(5,2,i)
#    if col !='pdays':
#        sns.distplot(bank[col])
#        i=i+1
#        plt.xticks(rotation=45)
#        plt.show()
#plt.tight_layout()
#plt.show()

# Bi variant analysis -> continous variable vs Target
i=1
for col in bank.select_dtypes(["int64","float64"]):
    plt.subplot(5,2,i)
    sns.distplot(bank.loc[bank.y=='yes',col],hist=False,kde=True,kde_kws={'shade': True, 'linewidth':3})
    sns.distplot(bank.loc[bank.y == 'no', col], hist=False, kde=True, kde_kws={'shade': True, 'linewidth': 3})
    i=i+1
plt.tight_layout()
plt.show()