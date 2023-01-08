'''def display(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
row2[1]='x'
print(display(row1,row2,row3))
result= input('please Enter the value:')
print(result)
print(type(result))
new_result=int(result)
print(type(new_result))
position_index=int(input("please select the index position"))
'''

def user_choice():
    choice='wrong'
    acceptable_values=range(0,10)
    within_range=False
    while choice.isdigit()==False or within_range==False:
        choice=input("please enter your choice 0-9:")
        if choice.isdigit()==False:
            print("sorry the entered number is invalid")
        if choice.isdigit()==True:
            if int(choice) in acceptable_values:
                within_range=True
            else:
                print("sorry,you're out of the accebtable values")
                within_range=False
    return int(choice)
print(user_choice())




