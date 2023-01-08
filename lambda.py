def square(num):
    return num**2
nums=[2,3,4,5,6]
for item in map(square,nums):
  print(item)
print(list(map(square,nums)))

def splicer(mystring):
    if len(mystring)%2==0:
        return  'Even'
    else:
        return mystring[0]
print(splicer('hamoud'))
names=['andy','hmoud','sami','hanan','sara']
for name in map(splicer,names):
    print(name)
print(list(map(splicer,names)))
def check_even(a):
    return a%2==0
aa=[3,4,5,666,7,8,88]
print(list(map(check_even,aa)))
print(list(filter(check_even,aa)))
for e in filter(check_even,aa):
    print(e)


def quad(q): return q**4
print(quad(2))

new=lambda qq:qq**4
print(new(5))
numbers=[3,4,5,6,7]
print(list(map(lambda  num:num**2 ,numbers)))
print(list(filter(lambda num:num%2==0,numbers)))
print(list(map(lambda f:f[0],names)))
print(list(map(lambda f:f[::-1],names)))
