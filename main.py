#  to intialize global variable
print("---------------------------------WELCOME TO THE TIC-TAC-TOE GAME----------------------------------")

game_still_on = True
winner = None
current_player = 'X'

# Name of the players
name1 = input("Enter the name of the player 1:")
name2 = input("Enter the name of the player 2:")

# values are assingning
print(name1+" has (X) "+"chance 1st.")
print(name2+" has (O) "+"chance 2nd.")

# display_board()
board  = ['_','_','_',
        '_','_','_',
        '_','_','_',]

# to display the board on screen 
def display_board():
    print(board[0]+'|'+ board[1]+'|'+board[2])
    print(board[3]+'|'+ board[4]+'|'+board[5])
    print(board[6]+'|'+ board[7]+'|'+board[8])



# play the game of tic tac toe
def play_game():

    display_board()
    while game_still_on:
        # handle the turn to the player
        handle_turn(current_player)

        # to the check the game is over
        game_is_over()

        # to flip the turn
        flip_the_chance()

# if the game is ended
    if winner == 'X' or winner == 'O':
        if(winner == 'X'):
         print(name1+" won")
        elif(winner == 'O'):
            print(name2+" won")
    else:
        print("Game tie.")
    

# to handle the turn 
def handle_turn(player):

    print(player +"'s turn")
    

    position = input("Enter the position 1 to 9:")
    
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        print("Invalid input")
        position = input("Enter the position 1 to 9:")
    
   
    position = int(position)-1


    while board[position] != '_':
        print("Can't Overwite")
        position = input("Enter the position 1 to 9:")
        position = int(position)-1

    board[position] = player
    display_board()

def game_is_over():
    check_if_win()
    check_if_tie()
    return

def check_if_win():
   global winner
    # check row
   row = check_rows()
    # check col
   col = check_col()
    # check diagonals
   diagonal = check_diagonals()

# to get the winner
   if row:
    #   global winner 
      winner = row
   elif col:
    #   global winner 
      winner = col
   elif diagonal:
    #   global winner 
      winner = diagonal
   else:
    #   global winner 
      winner = None

   return

   
def check_rows():
    global game_still_on

    row_1 = board[0] == board[1] == board[2] != '_'
    row_2 = board[3] == board[4] == board[5] != '_'
    row_3 = board[6] == board[7] == board[8] != '_'

    if row_1 or row_2 or row_3:
        game_still_on = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_col():
    global game_still_on

    col_1 = board[0] == board[3] == board[6] != '_'
    col_2 = board[1] == board[4] == board[7] != '_'
    col_3 = board[2] == board[5] == board[8] != '_'
    if col_1 or col_2 or col_3:
        game_still_on = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
   


def check_diagonals():
    global game_still_on

    dia_1 = board[0] == board[4] == board[8] !='_'
    dia_2 = board[6] == board[4] == board[2] !='_'
    if dia_1 or dia_2:
        game_still_on = False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[6]


def check_if_tie():
    global game_still_on
    if '_' not in board:
        game_still_on = False
    return
    
def flip_the_chance():
    global current_player
    if current_player =='X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return



play_game()

