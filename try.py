def add(n1,n2):
    return  n1+n2
try:
    number1=10
    number2=5
    #number2=input("please enter ther ")
    print(add(number1,number2))
except:
    print("sorry there is a mistake")
else:
    print("the addition has been done")

try:
    f=open('hm.txt','r')
    f.write('hello this is i')
except TypeError:
    print("there was a type error")
except OSError:
        print('hey u have an OS error')
finally:
    print('i always run')

def ask_for_int():
    while True:
     try:
            int(input("pls enter an  interger number"))
     except:
            print('wrong value')
            continue
     else:
           print("correct value ,Thank u")
           break
     finally:
            print('End of try/except/finally')
print(ask_for_int())