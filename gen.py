def create_cubes(n):
    #result=[]
    for x  in  range(n):
     #   result.append(x**3)
      yield x**3


print(create_cubes(4))
print(list(create_cubes(4)))
for x in create_cubes(4):
    print(x)

def gen_fib(n):
    a=1
    b=1
    for  i in range(n):
        yield a
        a,b = b,a+b
print(gen_fib(4))
for num in gen_fib(4):
    print(num)

def simple_gen():
    for x in range(3):
        yield x
for number in simple_gen():
    print(number)
g=simple_gen()
print(g)
print(next(g))
print(next(g))
s='hello'
for letter in s:
    print(letter)
ss_iter=iter(s)
print(next(ss_iter))
def gensquares(n):
    for i in range(n):
        yield i**2
for num in gensquares(4):
    print(num)




