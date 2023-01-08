#object  function .
my_list=['one','two','three']
my_list.append('four')
print(my_list)
my_list.pop()
my_list.pop(0)
print(my_list)
letters_list=['t','l','a','b','x','y','z','w']
letters_list.sort()
print(letters_list)
my_dic={
    'key1':'value1',
    'key2':'value2',
    'key3':'vlaue3',
}
print(my_dic)
print(my_dic['key2'])
prices={
    'apple':2.5 ,
     'milk':4 ,
     'sugar':5,
}
print(prices['sugar'])
dd={
    'k1':123,
    'k2':[1,3,5,"hm"] ,
    'k3':{'k4':'val'},
}
print(dd['k2'])
print(dd['k3']['k4'])
print(dd['k2'][2])
print(dd['k2'][3].upper()) # it will convert it to upper
dd['k5']=550
print(dd['k5'])
dd['k6']=340
print(dd)
dd.keys()
dd.values()
ddd=dd.items()
print(ddd)
tt=(1,2,3,4,5) #
ll=[2,'l',3,4]
print(type(tt))
print(type(dd))
print(type(ll))
tt=('t','s')
print(tt)
my_tuple=('a','b','c','d','a','a')
print(my_tuple.count('a'))
print(my_tuple.index('c'))
ll[0]=55
#tt[0]=55 can't assigb new index for the Tuples.

set(ll)
print(set(ll))
print(1==1)
print(1>2)
print(type(False))
x=None
print(x)
fff=frozenset('abcdefghijklmnopq')
print(fff)