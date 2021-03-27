""" This is a Connect Four game played by 2 players. """

import pandas as pd
import random

def check_color(c):
    if c not in colors:
        c = input(f'color values restricted to Red(R) and Black(B). Choose a new color: ')
        c = check_color(c)
    return c
    
def check_input(col):
    if col > 6:
        print('The number is too big.  It should be less than 7.')
        col = int(input(f'{player} please choose a column 0-6: '))
        col = check_input(col)
    if ' ' not in board[[col]].values:
        col = int(input(f'Column {col} is full, please pick another column: '))
        col = check_input(col)    
    return col

def play(col):
    """ Find a place for the next move."""
    col = check_input(col)
    for i in range(board.shape[0]-1, -1, -1):
        if board.iloc[i,col] == ' ':
            return i, col

def check_rules(idx, col, c):
    
    def check_row(idx, col, c):
        """This funciton checks if there are four consecutive color in a row. """
        counter = 1
        for i in range(col+1, board.shape[1]):
            if board.iloc[idx, i] == c:
                    counter +=1
                    if counter == 4:
                        print(f'Player {player} wins!')
                        return True
            else: 
                for i in range(col-1, -1, -1):
                    if board.iloc[idx, i] == c:
                        counter +=1
                        if counter == 4:
                            print(f'Player {player} wins!')
                            return True
                    else:
                        return False
                
    def check_col(idx, col, c):
        """This funciton checks if there are four consecutive color in a column. """
        counter = 1
        for i in range(idx+1, board.shape[0]):
            if board.iloc[i, col] == c:
                counter +=1
                if counter == 4:
                    print(f'Player {player} wins!')
                    return True
            else:
                return False
        for i in range(idx-1, -1, -1):
            if board.iloc[i, col] == c:
                counter +=1
                if counter == 4:
                    print(f'Player {player} wins!')
                    return True
            else:
                return False
            
    def check_diag(idx, col, c):
        """This funciton checks if there are four consecutive color diagonally. """
        counter = 1

        # check matches in upper right diagonal direction: r_decr, c_incr
        len1 = min(idx, board.shape[1]-col)
        for i in range(1,len1):
            if board.iloc[idx-i, col+i] == c:
                counter +=1
                if counter == 4:
                    print(f'Player {player} wins!')
                    return True
        
        # check matches in lower right diagonal direction: r_incr, c_incr
        len1 = min(board.shape[0]-idx, board.shape[0]-col)
        for i in range(1,len1):
            if board.iloc[idx+i, col+i] == c:
                counter +=1
                if counter == 4:
                    print(f'Player {player} wins!')
                    return True

        # check matches in upper left diagonal direction: r_decr, c_decr
        len1 = min(idx, col)
        for i in range(1, len1):
            if board.iloc[idx-i, col-i] == c:
                counter +=1
                if counter == 4:
                    print(f'Player {player} wins!')
                    return True

        # check matches in lower left diagonal direction: r_inc, c_decr
        len1 = min(board.shape[0]-idx, col)
        for i in range(1, len1):
            if board.iloc[idx+i, col-i] == c:
                counter +=1
                if counter == 4:
                    print(f'Player {player} wins!')
                    return True
            else:
                return False

    game_over = check_row(idx, col, c)
    if game_over == True:
        return game_over
    game_over = check_col(idx, col, c)
    if game_over == True:
        return game_over
    game_over = check_diag(idx, col, c)
    if game_over == True:
        return game_over
  
            
if __name__ == '__main__':

    # initialize game board with 6 rows and 7 columns
    board = pd.DataFrame(columns=range(7), index=range(6))
    board = board.fillna(' ')

    # initialize the game: pick first player and colors for the players
    colors = ['R', 'B']
    players = [1,2]
    idx = 5
    player = random.choice(players)
    print(f'player {player} will go first.', '\n')
        
    if player == 1:
        c1 = input(f'Player {player} please choose your color (R= red, B= black): ')
        c1= check_color(c1)
        print()
        c2 = [c for c in colors if c !=c1][0]
        col = int(input(f'{player} please choose a column 0-6: '))
        print()
        col = check_input(col)
        board.iloc[idx, col] = c1

    else:
        c2 = input(f'Player {player} please choose your color (R= red, B= black): ')
        c2= check_color(c2)
        print()
        c1 = [c for c in colors if c !=c2][0]
        col = int(input(f'Player {player} please choose a column 0-6: '))
        print()
        col = check_input(col)
        board.iloc[idx, col] = c2

    print(board)
    print()

    # play the game

    game_over = False
    while not game_over:
        # check if the board is filled
        if ' ' not in board.values:
            print('No more position to play.')
            break
        else:
            # determine the next player and the correponding color
            player = [p for p in players if p != player][0]

            # pick color
            if player == 1:
                c = c1
            else:
                c = c2

            # next move by a player   

            col = int(input(f'Player {player} please choose a column 0-6: '))
            print()
            col = check_input(col)
            idx, col = play(col)
            board.iloc[idx, col] = c
            print(board)
            print()
            game_over = check_rules(idx, col, c)
            if game_over == True:
                print('Game over!')
                break