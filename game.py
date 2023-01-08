game_list=[1,2,3]
def display_game(game_list):
    print("Here is the  game list")
    print(game_list)
def position_choice():
    choice='wrong'
    while choice not in ['0','1','2']:
        choice=input("pick a position (0,1,2) : ")
        if choice not in ['0','1','2']:
            print("sorry you picked an invalid choice")
    return  int(choice)
def replace_choice(game_list,position):
    user_replacment=input('type a string to be replaced: ')
    game_list[position]=user_replacment
    return  game_list



print(display_game(game_list))
print(position_choice())
print(replace_choice(game_list,position=1))