game_list = [1, 2, 3]
def gameon_choice():
    choice = 'wrong'
    while choice not in ['y','n']:
        choice=input("keep playing ,choose n or y : ")
        if choice not in ['y','n']:
            print("sorry you picked an invalid choice")
    if choice == 'y':
        return True
    else:
        return False

def display_game(game_list):
    print("Here is the  game list")
    print(game_list)


def position_choice():
    choice = 'wrong'
    while choice not in ['0', '1', '2']:
        choice = input("pick a position (0,1,2) : ")
        if choice not in ['0', '1', '2']:
            print("sorry you picked an invalid choice")
    return int(choice)

def replace_choice(game_list,position):
    user_replacment=input('type a string to be replaced: ')
    game_list[position]=user_replacment
    return  game_list

game_on=True
while game_on:
    display_game(game_list)
    position=position_choice()
    game_list=replace_choice(game_list,position)
    display_game(game_list)
    game_on=gameon_choice()  # as gameon_choice will has as a result true or false then game_on is T  or F

print(gameon_choice())
