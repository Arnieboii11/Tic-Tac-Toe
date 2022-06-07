#TIC-TAC-TOE GAME 

import random
from time import sleep
#creating a matrix

boxes = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ]
user = 'X'
bot = '0'
player1 = user
turn = 1
win_poss = [  [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], ]

#function to print the board

def print_board(initial=False):
    print(('''
{} | {} | {}
-------------
{} | {} | {}
-------------
{} | {} | {}

        ''').format(*([x for x in range(1, 10)] if initial else boxes)))

#function to accept an input from the user till the entered input is correct

def take_turn(player, turn):
    while True:
        if player is bot:
            box = get_bot_move()
        else:
            box = input('Player %s, type a number from 1-9 to select a box: ' % player)

            try:
                box = int(box) - 1 # subtract 1 to sync with boxes[] index numbers
            except ValueError:
                # Not an integer
                print('That\'s not a valid number, try again.\n')
                continue

        if box < 0 or box > 8:
            print('That number is out of range, try again.\n')
            continue

        if boxes[box] == ' ':# initial value
            boxes[box] = player # set to value of current player
            break
        else:
            if player == user:
                print('That box is already marked, try again.\n')
        
#function to select a random tile from the computer

def get_bot_move():
    return random.randint(0,8)
        
#function to change the turns

def switch_player(turn):
    current_player = bot if turn % 2 == 0 else user
    return current_player

#function to check that when the user or the bot has won

def check_for_win(player, turn):
    if turn > 4: # need at least 5 moves before a win is possible
        for combo in win_poss:
            score = 0
            for index in combo:
                if boxes[index] == player:
                    score += 1
                if score == 3:
                    return 'win'

        if turn == 9:
            return 'tie'

#function to play the game

def play(player, turn):
    while True:
        take_turn(player, turn)
        print_board()
        result = check_for_win(player, turn)
        if result == 'win':
            print('Game over. %s wins!\n' % player)
            break
        elif result == 'tie':
            print('Game over. It\'s a tie.\n')
            break
        turn += 1
        player = switch_player(turn)

# Begin the game:

print('\n\nWelcome to Tic Tac Toe!')
print_board(initial=True)
print('\n\n Starting the Game...')
sleep(2)
play(player1, turn)