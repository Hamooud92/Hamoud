def unique(ist):
    return list(set(list(ist)))
print(unique([1,2,111,2,1,2,4,5,5,6,7,7,7]))

def new_unique(s):
    x=[]
    for n in s:
        if n  not in x:
            x.append(n)
    return x
print(new_unique([1,2,3,3,3,4,4,4,5,6]))

def multiply(numbers):
    total=1
    for num in numbers:
        total=total*num
    return total
print(multiply([1,2,2,3,4]))

def palindrome(pp):
    pp=pp.replace(' ','')   #replace the space with no space, the purpose to remove the spaces  .
    #check the current list equal to its reverse
    return pp==pp[::-1]  #pay attention to the comparsion not to the  assiment

import string
def ispangram(str1,alphabet=string.ascii_lowercase):

    #create the set word of alphabet
    #remove spaces
    #convert all to in lowercase
    #grab all unique letters
    alphaset=set(alphabet)
    str1=str1.replace(' ','')
    str1 = str1.lower()
    str1=set(str1)
    return str1 == alphaset
print(ispangram("the quick brown fox jumps over the lazy dog"))




