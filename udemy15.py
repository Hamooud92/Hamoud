def myfunc(a,b):
    return sum((a,b))*0.5
a=myfunc(2,3)
print(a)

def myfunc(a,b,c=0,d=0):   #this is default values to take from it in case didn't assign anyvalue .
    return sum((a,b,c,d))*0.5
a1=myfunc(2,3,10)
print(a1)

def myfunc1(*args):  #can be changed to be anyword like *spam ,*nums and so...
    print(args)
    return sum(args)
a2=myfunc1(2,3,4,1)
print(a2)

def myfunc(**kwargs):  #kwargs can be cahnged
    print(kwargs)
    if 'fruit' in kwargs:
        print('my fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('no okk have anyk')
c=myfunc(fruit='apple',veg='tomatos',dessert='baklawa')  #dictionary  k:'value'
print(c)
def myfunc(*args,**kwargs):  #the order is important
    print(args)
    print(kwargs)
    print("i would like to {} pices  of {}".format(args[0],kwargs['food']))
d=myfunc(10,2,33,fruit='org',food='rice')  #the order is important
print(d) 