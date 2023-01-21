import random

# Display the playing field passed in as a list
def display_board(board):

    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])

# Test board
# test_board = ["#", "", "O", "X", "O", "X", "O", "X", "O", "X"]

# Player 1 chooses their board marker
def player_input():
    while (True):
        
        choice = input("\nPlayer1: Choose 'X' or 'O'!  ")
    
        if choice == "X" or choice == 'x':
            player1_marker = "X"
            player2_marker = "O"
            break

        elif choice == "O" or choice == 'o':
            player1_marker = "O"
            player2_marker = "X"
            break
    
    print(f"\nPlayer 1: {player1_marker} \nPlayer 2: {player2_marker}\n")
    return player1_marker, player2_marker


# Function to mark board with players' moves
def place_marker(board, marker, position):
    board[position] = marker


# Function to check if player wins each turn
def win_check(board, marker):
    if (board[1] == marker and board[2] == marker and board[3] == marker):
        return True
    elif (board[4] == marker and board[5] == marker and board[6] == marker):
        return True 
    elif (board[7] == marker and board[8] == marker and board[9] == marker):
        return True 
    elif (board[1] == marker and board[4] == marker and board[7] == marker):
        return True
    elif (board[2] == marker and board[5] == marker and board[8] == marker):
        return True
    elif (board[3] == marker and board[6] == marker and board[9] == marker):
        return True
    elif (board[1] == marker and board[5] == marker and board[9] == marker):
        return True 
    elif (board[3] == marker and board[5] == marker and board[7] == marker):
        return True
    else:
        return False

# Randomly chooses which player goes first
def choose_first():
    x = random.randint(1,2)
    if x == 1: 
        print("Player 1 goes first!")
        return 1
    else:
        print("Player 2 goes first!")
        return 2


# Checks if space on the board chosen by player is taken or free
def free_space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


# Checks if board is full (tie game since no spaces left)
def full_board_check(board):
    for item in board:
        if item == ' ':
            return False

    return True


# Player chooses a position to place marker 
def player_choice(board):
    while True:
        try: 
            position = int(input("Choose a position (1-9): ").strip())
        except ValueError:
            print("Invalid choice!")
            continue
        else:

            if position > 9 or position < 1 or position % 1 != 0:
                print("Invalid choice!")
                continue
            else:
                break

    if (free_space_check(board, position)):
        return position

    else:
        print("Spot already taken! Choose a different location!")


# Ask to play again? 
def replay():

    while True:
        answer = input("Would you like to play again? Y or N? ")
        
        if answer.lower() == 'yes' or answer.lower() == 'y':
            return True
        elif answer.lower() == 'no' or answer.lower() == 'n':
            return False
        else:
            print("\nSorry, I didn't quite get that...\n")
            continue


def main():
    game_on = True

    # Set up empty board
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #Initialize scoreboard
    player1_score = 0
    player2_score = 0
    draws = 0

    # Welcome text
    print('\nWelcome to Tic Tac Toe!\n')

    # Run game repeatedly unless 'break'
    while True:

        print('------------')
        print('Scoreboard ')
        print('------------')
        print(f'Player 1: {player1_score}')
        print(f'Player 2: {player2_score}')
        print(f'Draws:    {draws}')
        print('------------')

        # Select player_markers
        player1_marker, player2_marker = player_input()

        # Select who goes first and set variables
        if (choose_first() == 1):
            first = player1_marker
            second = player2_marker
        else:
            first = player2_marker
            second = player1_marker

        # While loop for the actual game 
        while game_on:
            choice = None
            # Turn for whoever is 'first'
            print('')
            display_board(board)
            print('\n')
            
            while choice is None:
                choice = player_choice(board)

            place_marker(board, first, choice)

            # Check if player's turn won the game
            if (win_check(board, first)):
                display_board(board)

                if (first == player1_marker):
                    player1_score += 1
                    print(f"\nPlayer 1 wins!\n")
                else:
                    player2_score += 1
                    print(f"\nPlayer 2 wins!\n")
                break
            
            # Check if player's turn ended the game in a tie
            elif (full_board_check(board)):
                display_board(board)
                print('\nDraw!\n')
                draws += 1
                break

            # Turn for whoever got 'second' (Exact same as 'first')
            choice = None

            print('')
            display_board(board)
            print('\n')

            while choice is None:
                choice = player_choice(board)

            place_marker(board, second, choice)


            if (win_check(board, second)):
                display_board(board)

                if (second == player1_marker):
                    player1_score += 1
                    print(f"\nPlayer 1 wins!\n")
                else:
                    player2_score += 1
                    print(f"\nPlayer 2 wins!\n")
                break


            elif (full_board_check(board)):
                display_board(board)
                print('\nDraw!\n')
                draws += 1
                break

            # No wins or draws in both first and second's turns == continue the game_on loop
            else:
                continue

    
        if (replay()):
            board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            continue
        else:
            print('------------')
            print('Final Score')
            print('------------')
            print(f'Player 1: {player1_score}')
            print(f'Player 2: {player2_score}')
            print(f'Draws:    {draws}')
            print('------------')
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()