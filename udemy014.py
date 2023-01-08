def myfunc(a,b,c,d=0,e=0):
    return (float(sum((a,b,c,d,e))*0.05))
print(myfunc(40,60,100))

def myfun1(*args):
    print(args)    #it will print the arguments as tuple .
    for item in args:
        print(item)
    return sum(args)*2
print(myfun1(2,3,1))

def myfun2(*spam):
    print(spam)    #it will print the arguments as tuple .
    for  ss in spam:
        print(ss)
    return sum(spam)*2
print(myfun2(4,5,6))

def myfun3(**kwargs): #dictionary
    print(kwargs)
    if 'fruit' in kwargs:
        print('my choice is  {}'.format(kwargs['fruit']))
    else:
        print('no  find any fruit here')
print(myfun3(fruit='apple',veg='lettuce'))

def myfun8(*args,**kwargs):
    print(args)
    print(kwargs)
    print('i would like {} {}'.format(args[0],kwargs['food']))
    print('i would like {} {}'.format(args[1], kwargs['animal']))
print(myfun8(10,20,30,fruit='orange',food='eggs',animal='cat'))





