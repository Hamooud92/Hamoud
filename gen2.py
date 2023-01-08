import random
random.randint(1,10)
def num_ran(low,hight,n):
    for i in range(n):
        yield random.randint(low,hight)
for num in num_ran(1,10,12):
    print(num)

s='hello'
s=iter(s)
print(next(s))
my_list=[1,2,3,4,5]
gencomp=(item for item in my_list if item >3)
for item in  gencomp:
    print(item)