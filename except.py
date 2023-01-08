try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("error")

try:
    x=5
    y=0
    z=x/y
    print(z)
except ZeroDivisionError:
    print("this is Zero division error ")
finally:
    print("All done")

def ask():
    waiting=True
    while waiting:
        try:
            n=int(input("enter a number"))
        except:
            print("wrong number")
            continue
        else:
            waiting=False
        finally:
            print("done")
print(ask())