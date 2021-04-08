s="geeksofrgeeks"
from collections import Counter
ctr=Counter(s)
#print(type(ctr))
print(ctr)
for key,value in ctr.items():
    if value == 1:
        print(key)
        break