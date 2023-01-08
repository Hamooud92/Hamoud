from random import  shuffle
from random import  randint
kkk=[1,2,3,,6,44,5,66]
for num in range(2,12,3):
    print(num)
a=list(range(2,12,3))
print(a)
index_count=0
for letter in 'abcdefghklmn':
    print('at index {} the letter is {}'.format(index_count,letter))
    index_count+=1
new_counter=0
for inexer in 'hamoud alkrhoot':
    print('the indexer {} is for the character {}'.format(new_counter,inexer))
    new_counter+=1
new_index=0
word='hamouda'
for lll in word:
    print(word[new_index])
    new_index+=1
my_word='hamoudy'
for item in enumerate(my_word):
    print(item)
for letter,index in enumerate(my_word):
    print(letter,index)
    print(letter)
    print(index)
    print('\n')
list1=[1,2,3]
list2=['a','b','c']
for item in zip(list1,list2):
    print(item)
print(list(zip(list1,list2)))

check = 'x' in ['x','g','z','y']
print(check)
print(kkk)
print(randint(0,100))
hm=input('enter your name')
print(hm)


def front_times(str, n):
    fl = 3
    if fl > len(str):
        fl = len(str)
    front = str[:fl]
    r = ""
    for i in range(n):
        r = r + front
    return r
eee=front_times('hms',9)
print(eee)