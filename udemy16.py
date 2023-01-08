def myfunc(*args):
    lista=[]
    for i in args:
      if i%2==0:
         lista.append(i)
    return lista
print(myfunc(2,4,5,6))