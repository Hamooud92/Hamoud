test_board = ['#', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']
def display_board(board):
    print('  | |')
    print(' '+board[7]+'|'+board[8]+'|'+board[9])
    print('  | |')
    print('  '+board[4]+'|' + board[5]+'|'+board[6])
    print('  | |')
    print(' ' +board[1]+'|'+board[2]+'|'+board[3])
    print('  | |')

display_board(test_board)
print('\n'*100)

def player_input():
    marker=''
    while not(marker=='O' or marker=='X'):
        marker=input('player1:do you want to be x or o?: ').upper()
    if marker=='X':
         return('X','O')
    else:
        return ('O','X')
print(player_input())


def place_marker(board,marker,position):
    board[position]=marker
place_marker(test_board,'$',6)
display_board(test_board)
#this will return True
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
win_check(test_board,'X')
import random
def choose_first():
    if random.randint(0,1)==0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board):
    return board[position]==''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choise(board):
    position= 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('choose your position from 1-->9'))
    return  position
def replay():
    return input('do you want to play again? Enter yes or no').lower().startswith('y')
print('welcome to Tic tac toe!')
while True:
    theboard=['']*10
    player1_maker,player2_maker=player_input()
    turn=choose_first()
    print(turn+'will go first')
    play_game=input('Are u ready to play? :')
    if play_game.lower()[0]=='y':
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == 'player1':
            display_board(theboard)
            position=player_choise(theboard)
            place_marker(theboard,player1_maker,position)
        if win_check(theboard,player1_maker):
            display_board(theboard)
            print('congrtulation ! you have won the game')
            game_on=False
        else:
            if full_board_check(theboard):
                display_board(theboard)
                print("the game is a adraw")
                break
            else:
                turn='player 2'
    else:
        display_board(theboard)
        position=player_choise(theboard)
        place_marker(theboard,player1_maker,position)
        if win_check(theboard,player2_maker):
            display_board(theboard)
            print('player 2 is the winer')
            game_on=False
        else:
            if full_board_check(theboard):
                display_board(theboard)
                print('the game is a draw')
                break
            else:
                turn='player1'
    if not replay():
     break

'''


































