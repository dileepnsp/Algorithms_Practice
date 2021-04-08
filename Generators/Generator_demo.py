# Generators wont be stored in memory... Yield from function.
#Generators are lazy evolution..
#Function

import sys
def function(lst):
    result=[]
    for a in lst:
        result.append((a*3))
    return result

def generator(lst):
    for a in lst:
        yield a*3

print(function([1,3,5,7]))
print(list(generator([2,31,15,17])))

fun_return=[a*3 for a in [2,3,5,6]]
generator_return=(a*3 for a in [2,3,5,6])

print(fun_return)
print(list(generator_return))

print(list(generator_return))
print(sys.getsizeof(fun_return))
print(sys.getsizeof(generator_return))

print("iterate generator")
for a in list(generator_return):
    print(a)

def infinite_seq():
    num=0
    while True:
        yield num
        num+=1
gen=infinite_seq()

print(next(gen))
print(next(gen))
print(next(gen))
print(gen.__next__())

for a in iter(gen):
    print(a)