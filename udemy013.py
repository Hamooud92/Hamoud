from random import shuffle
example=[1,2,3,4,5,6,7]
result=shuffle(example)
print(result)
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
mylist=['1',33,4,'t','z']
result=shuffle_list(example)
print(result)
print(shuffle_list(mylist))

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input('pick a number:0,1,2')#input always return a string
    return  int(guess)
print(player_guess())
new_list=['','o','']
mixup=shuffle_list(new_list)
guess=player_guess()
def check_guess(new_list,guess):
    if mylist[guess]=='o':
        print('correct')
    else:
        print('wrong')
        print(new_list)
print(check_guess(mixup,guess))


