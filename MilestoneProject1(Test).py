import random


# To display the board of the game
def display_board(text):
    print(text[7].rjust(2, ' ') + "|" + text[8].rjust(2, ' ') + "|" + text[9].rjust(2, ' '))
    print('--|--|--')
    print(text[4].rjust(2, ' ') + "|" + text[5].rjust(2, ' ') + "|" + text[6].rjust(2, ' '))
    print('--|--|--')
    print(text[1].rjust(2, ' ') + "|" + text[2].rjust(2, ' ') + "|" + text[3].rjust(2, ' '))


# To randomly decide which Player among 1 and 2 goes first
def first_player():

    if first == 1:
        print('Player 1 starts!')
    else:
        print('Player 2 starts!')


# To accept the players' marker choices(X/O)
def player_input():
    global p1_choice
    global p2_choice
    marker = ''
    while marker != 'X' and marker != 'O':
        if first == 1:
            marker = input("Player 1:Enter your choice(X/O):")

            p1_choice = marker
            if p1_choice == 'X':
                p2_choice = 'O'
            else:
                p2_choice = 'X'
            print("Player 2 Choice:", p2_choice)
        else:
            marker = input("Player 2:Enter your choice(X/O):")

            p2_choice = marker
            if p2_choice == 'X':
                p1_choice = 'O'
            else:
                p1_choice = 'X'
            print("Player 1 Choice:", p1_choice)


# To place the markers on the board according to players' desired positions
def place_marker():
    if first == 1:
        p1_pos = int(input("Player 1 enter position:"))
        board[p1_pos] = p1_choice
        if win_check() == 'Player 1':
            pass
        else:
            p2_pos = int(input("Player 2 enter position:"))
            board[p2_pos] = p2_choice
    else:
        p2_pos = int(input("Player 2 enter position:"))
        board[p2_pos] = p2_choice
        if win_check() == 'Player 2':
            pass
        else:
            p1_pos = int(input("Player 1 enter position:"))
            board[p1_pos] = p1_choice

    print(board)  # Just printing the 'board' list for reference


# To check the winner(if any)
def win_check():
    if (p1_choice == board[1] == board[2] == board[3] or p1_choice == board[4] == board[5] == board[6] or
            p1_choice == board[7] == board[8] == board[9] or p1_choice == board[1] == board[4] == board[7] or
            p1_choice == board[2] == board[5] == board[8] or p1_choice == board[3] == board[6] == board[9] or
            p1_choice == board[1] == board[5] == board[9] or p1_choice == board[3] == board[5] == board[7]) :

        return 'Player 1'
    elif (p2_choice == board[1] == board[2] == board[3] or p2_choice == board[4] == board[5] == board[6] or
          p2_choice == board[7] == board[8] == board[9] or p2_choice == board[1] == board[4] == board[7] or
          p2_choice == board[2] == board[5] == board[8] or p2_choice == board[3] == board[6] == board[9] or
          p2_choice == board[1] == board[5] == board[9] or p2_choice == board[3] == board[5] == board[7]) :
        return 'Player 2'
    else:
        return 'Draw'


# To check for empty spaces on the board, and accept next moves only if space available
def space_check(board):
    if board[1] == '1' or board[2] == '2' or board[3] == '3' or board[4] == '4' or board[5] == '5' or board[6] == '6' \
            or board[7] == '7' or board[8] == '8' or board[9] == '9':
        return True
    else:
        return False


# To check if user wants to replay the game
def replay():
    again = input("Do you want to play again? (Y/N) :")
    if again == 'Y':
        return True
    else:
        return False

# Finished setup

# Game begins


while True:

    print("The places in the board are numbered in the following way:-")
    display_board(['#', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

    board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(board)

    game_on = True

    first = random.randint(1, 2)

    first_player()

    player_input()

    while game_on:

        space_check(board)
        if space_check(board):
            if win_check() == 'Player 1':
                print("Player 1 wins!")
                break
            elif win_check() == 'Player 2':
                print("Player 2 wins!")
                break
            else:
                place_marker()
                display_board(board)
        else:
            if win_check() == 'Player 1':
                print("Player 1 wins!")
                break
            elif win_check() == 'Player 2':
                print("Player 2 wins!")
                break
            else:
                print("It's a draw!")
                break

    if replay():
        pass
    else:
        print("You have exited the game.")
        break
