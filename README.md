# CS50p Final Project: TicTacToe

### Video Demo: <URL HERE>

# Description: 

### Rules of the Game
This project is a simulation representing the popular game of 'TicTacToe', played by players using the command line. In this game, two players are each designated a marker, usually selected to be "X" and "O". They then take turns placing their respective markers on the boards in one of the nine empty slots, until one player gets three of their markers in a row. The markings can be three in a row vertically, horizontally, or diagonally to win. The game also has the chance to end in a draw in the event that both players fill up the entire board with their marker without either achieving three in a row. 

### Display Board
This is a simple function used to display the board being played on and keeping track/updating as each players fills the board up with their marker during each turn. It is ran by creating an array with 10 empty slots and calling them in a series of print functions. 

The first slot "board[0]" is not used to generate and display the board being played on. This keeps player's inputs for choosing a spot on the board more simple and resembling a typical number keypad (1-9 rather than 0-8).

### Player Input 
This function initializes the game by asking player 1 to choose his marker to be either "X" or "O". What player 1 chooses automatically sets their and player 2's markers and prints a statement that indicates which one was selected. 

### Place Marker
The place marker function takes in three arguments - the board, the marker, and the position. As arguably the most simple function in this program, all place_marker does is index into the 'position' argument of the 'board' argument, and replace the empty space with whatever marker, either "X" or "O". 

### Win check
Win check takes in the board and the marker and checks if the last turn won the game or not. By using a long checklist of conditional statements, this function checks every combination of patterns possible and returns a boolean depending on if the marker that last went won or not. 

### Choose First
The choose_first function helps with initializing the game in the beginning. It requires the random module to be imported and uses random.randint to "randomly" select either 1 or 2 as an integer. If 1 was selected, player 1 will have the first turn, and vice versa if 2 was selected. 

### Free Space Check
This function is used to check whether the space on the board that a player chooses to place their marker on is already taken or not. The board starts with space characters acting as empty spots on a 3x3 board. When a player selects a spot, it is replaced with their chosen marker, either "X" or "O". If a spot is chosen and is already filled with an "X" or "O", then this function returns false. Otherwise, it returns true. 

### Full Board Check 
This function checks whether the entire board is filled up or not after the win_check function is used to determine if the last turn won the game or not. If the last turn did not win the game, then this function is called to see if the game should end in a draw or continue for the next player's turn. 

It works by iterating through each of the index positions in the board and checking a conditional that checks if the position is a space character or not. If atleast one position equals an empty space, that means there is still a space left to place a marker in and the game may continue. This results in this function returning false. If the for-loop iterates through every position on the board without returning false, then none of the positions are empty, meaning the game ended in a draw since there are no spaces the player's may choose out of anymore. This returns true and ends the game. 

### Player Choice
This function is the heart of the game itself and represents each turn a player makes. A while loop is ran with a try/except statement containing an input function for the player to choose the position to place their marker for their turn. The try/except helps with ValueErrors incase the player inputs something other than an integer. The while loop runs until the player inputs a valid selection (i.e. not a string and not a decimal). After inputting a valid position, the while loop is broken and the free_space_check function is called to make sure the position chosen is not already chosen on the board. If it isn't, the function returns the position chosen. 

### Replay 
This function is called at the end of a match after one of the player's wins, or after a draw. It asks whether the players want to play again or not, and restarts or ends the game based on the answer inputted. 

### Main
The main function sets all of these mentioned functions in an order that makes sense to allow the game to run properly.

Starting with initializing the game, a scoreboard is generated with scores and draws set to equal 0. A welcome message is printed and the players are designated their markers using the 'player_input' function. Lastly, the 'choose_first' function selects which player goes first and which player goes second. 

Next, an outer while-loop is run for while the program is running. The empty board is displayed and the player randomly chosen to go first makes their move. After the position is chosen, the marker is set on the board position chosen by that player. After this turn, 'win_check' and 'full_board_check' are called to determine if that move won that player the game, or if the board is full and the game results in a draw. This obviously won't be the case for the first few turns, but is called nonetheless after each player goes to check in future turns as well. 

If the player neither wins, nor ties, the same pattern of steps occur but for the player chosen to go second. Again 'win_check' and 'full_board_check' are called to check whether this player won or tied with the last turn. This sequence of functions repeats until one of the two functions return True. 

When a player wins, their counter for the scoreboard is incremented by 1. If the game ends in a draw, the draw variable is incremented by 1. At the conclusion of that game, the 'replay' function is called to ask if the player's would like to play again or not. If they select yes, the while-loop continues and another game is played while updating the scoreboard. If they select no, the game ends, thanks the players for playing, and prints the final scoreboard.