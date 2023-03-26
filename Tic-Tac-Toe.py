board_list = [' ',' ',' ',' ',' ',' ',' ',' ', ' ']
def display(board = board_list):
    '''
    This function displays the current state of the board
    Input is a list of 9 values
    '''
    print('     |     |     ')
    print(f'  {board[0]}  |  {board[1]}  |  {board[2]}  ')
    print('-----|-----|-----')
    print(f'  {board[3]}  |  {board[4]}  |  {board[5]}  ')
    print('-----|-----|-----')
    print(f'  {board[6]}  |  {board[7]}  |  {board[8]}  ')
    print('     |     |     ')


def player_move(player):
    '''
    This function takes in user input and validates it 
    '''
    move = ''
    playable = False
    while move.isdigit() == False or playable == False:
        move = input('Please choose your move (1-9)') 
        if move.isdigit() == False:
            print("That's not a number")
            continue
        
        if int(move) not in [1,2,3,4,5,6,7,8,9]:
            print("Not in range")
            continue
        if board_list[int(move) - 1] != ' ':
            print('Space taken')
            continue
        playable = True
    
    if player == 1:
        board_list[int(move)-1] = 'X'
    elif player == 2:
        board_list[int(move)-1] = 'O'


def long_check(player,board=board_list):
    '''
    This function checks if either player has won
    '''
    if player == 1:
        if board_list[0] == "X" and board_list[1] == "X" and board_list[2] == "X":
            return True
        elif board_list[0] == "X" and board_list[3] == "X" and board_list[6] == "X":
            return True
        elif board_list[0] == "X" and board_list[4] == "X" and board_list[8] == "X":
            return True
        elif board_list[1] == "X" and board_list[4] == "X" and board_list[7] == "X":
            return True
        elif board_list[2] == "X" and board_list[5] == "X" and board_list[8] == "X":
            return True
        elif board_list[3] == "X" and board_list[4] == "X" and board_list[5] == "X":
            return True
        elif board_list[6] == "X" and board_list[7] == "X" and board_list[8] == "X":
            return True
        elif board_list[2] == "X" and board_list[4] == "X" and board_list[6] == "X":
            return True

    if player == 2:
        if board_list[0] == "O" and board_list[1] == "O" and board_list[2] == "O":
            return True
        elif board_list[0] == "O" and board_list[3] == "O" and board_list[6] == "O":
            return True
        elif board_list[0] == "O" and board_list[4] == "O" and board_list[8] == "O":
            return True
        elif board_list[1] == "O" and board_list[4] == "O" and board_list[7] == "O":
            return True
        elif board_list[2] == "O" and board_list[5] == "O" and board_list[8] == "O":
            return True
        elif board_list[3] == "O" and board_list[4] == "O" and board_list[5] == "O":
            return True
        elif board_list[6] == "O" and board_list[7] == "O" and board_list[8] == "O":
            return True
        elif board_list[2] == "O" and board_list[4] == "O" and board_list[6] == "O":
            return True
    
    if (" " in board_list) == False:
        return "full"

    return False

def check_win():
    '''
    This functions uses the long_check function to return an output back to the game 
    '''
    if long_check(1,board_list) == "full":
        print("It's a tie!")
        return True
    elif long_check(1,board_list) == True:
        print('Player one wins!')
        return True
    elif long_check(2,board_list) == True:
        print('Player two wins!')
        return True
    return False

def keep_playing():
    play = ' '
    while not (play in 'yn'):
        play = input("Play Again? (y/n)")
    if play == 'y':
        global board_list
        board_list = [' ',' ',' ',' ',' ',' ',' ',' ',' '] 
        display(['1','2','3','4','5','6','7','8','9'])
        return True
    elif play == 'n':
        return False      

if __name__ == '__main__':     
    game_on = True 
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    display(['1','2','3','4','5','6','7','8','9'])
    while game_on:
        player_move(1)
        display(board_list)
        if check_win() == True:
            if keep_playing() == True:
                continue
            else:
                break
        player_move(2)
        display(board_list)
        if check_win() == True:
            if keep_playing() == True:
                continue
            else:
                break