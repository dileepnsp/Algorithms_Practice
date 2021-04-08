from operator import itemgetter
d = {'a': 10, 'b': 20, 'c': 5, 'e': 8, 'd': 5}
# sort by values
print(sorted(d.items(),key=lambda x:x[1]))

# sort by values
print(sorted(d.items(),key=itemgetter(1)))

# sort by key
print(sorted(d.items(), key=itemgetter(0)))

# sort by key

print(sorted(d.items()))

print(sorted(d, key=d.get))

###########################
#Occurrence Counter in List:
###########################

from collections import Counter
lst=[1,1,1,2,3,4,5,2,3,3,4,7,10]
cnt=Counter(lst)
print(cnt)
print(cnt.most_common(1))

str_lst = ['blue', 'red', 'green', 'blue', 'red', 'red', 'green']
print(dict(Counter(str_lst)))

####################
#Powerful One-Liner:
####################

salary = 4000

if salary > 9000:
    tax = 900
elif 3000 < salary < 9000:
    tax = 100
else:
    tax = 0

print(tax)

tax=  900 if salary > 9000 else 100 if 3000 < salary < 9000 else 0
print(tax)

####################
#for loop Minimized:
####################

lst=[1,2,3]
doubled=[]
for i in lst:
    doubled.append(i*2)
print(doubled)

doubled=[i*2 for i in lst]
print(doubled)

###########
lst = ['a', 'b', 'c', 'd']
for index, value in enumerate(lst):
    print(f"{index}, {value}")
for index, value in enumerate(lst, start=10):
    print(f"{index}, {value}")

###############
colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3, 4]
for color, code in zip(colors, codes):
    print(f"{code}, {color}")

colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3]
for color, code in zip(colors, codes):
    print(f"{code}, {color}")

from itertools import zip_longest
colors = ["red", "green", "yellow", "blue"]
codes = [1, 2, 3, 4, 5, 6]
for color, code in zip_longest(colors, codes):
    print(f"{code}, {color}")
for color, code in zip_longest(colors, codes, fillvalue='Nothing'):
    print(f"{code}, {color}")

#Reverse a String or List

a = "humanbeing"
print(a[::-1])

#Join String and List Together

print('#'.join(a))

numbers = [1, 2, 3, 4, 5]
print(numbers)
#print('#'.join(numbers))
print('#'.join(map(str, numbers)))

#Swapping Values
a, b = 9, 10
a, b = b, a
print(a, b)

#for and else

a = [1, 2, 3, 4, 5]
# else gets called only when for loop does not reach break statement
for each in a:
    if each == 0:
        break
else:
    print('break statement did not executed')

#Checking Anagram
from collections import Counter
print(Counter('below'))
print(Counter('elbow') == Counter('below'))
print(Counter('study') == Counter('night'))

#Merge Dictionaries

d1 = {'a': 1}
d2 = {'b': 2}
print(dict(d1.items() | d2.items()))
print({**d1, **d2})
d1.update(d2)
print(d1)


######
lst=[1,3,5,7,9]
new_lst=[]
for i in lst:
    new_lst.append(i*2)
print(new_lst)

print(list(map(lambda x:x*2,lst)))
