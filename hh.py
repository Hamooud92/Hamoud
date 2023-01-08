import keyword
print(keyword.kwlist)
a=2
print(type(a))
b=9223555654654466
print(type(b))
pi=3.14
print(type(pi))
c='s'
print(type(c))
name='john'
print(type(name))
q=True
print(type(q))
z=False
print(type(z))
x=None
print(type(x))
num1,num2,num3=33,44,77
print(num1,num2,num3)
n1,n2,_ =1,4,5
print(n1,n2,_)
v=u=[22,44,55,66,77]
print(v)
v[0]=8
print(v)
print(u)
ll=[9,8,6,[3,41,3,2],5,3]
print(ll)
print(ll[0])
print(ll[3])
print(ll[3][1])

def my_fun():
    a=2
    return a
print(my_fun())
if a>b:
    print(a)
else:
    print(b)
def do_later():
    pass
sub=issubclass(bool,int)
print(sub)
ins1=isinstance(True,bool)
ins2=isinstance(False,bool)
print(ins2)
bbb=True+False
print(bbb)
print(True*False)
print(True*True)
print(type('hello'))
i=4
if isinstance(i,int):
    i+=1
    print(i)
elif  isinstance(i,str):
    i=int(i)
    i+=1

x=None
if x is None:
    print("x is None")

