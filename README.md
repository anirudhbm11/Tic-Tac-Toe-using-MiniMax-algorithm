# Tic-Tac-Toe-using-MiniMax-algorithm

GL Login: VM21013 <br />
Full Name: Anirudh Balaiah Mahesh <br />

## Project description
This project aims in creating a program which allows user to give option of playing
tic-tac-toe game in single player or multiplayer mode. The multiplayer mode can be
used to play the game where 2 humans are involved in the game. In the single player
game, the opponent will be computer which uses MiniMax AI algorithm in solving the
tictac toe.

## Goal
The goal of this project is to design an efficient algorithm which can be used by a 
computer in defeating a human in tic-tac-toe. Same algorithm can be further used in
creating chess or checkers engine.

## Interest for the problem
Tic tac toe has been a game which was present in almost all mobile phones. The computer always seemed to find the best move in all scenarios. I took up this project in order to learn the algorithm behind solving this game. This algorithm can be further usind in solving more difficult problems like chess and checkers.

## Algorithm and approach of solving the problem
* User input is taken to see if the user wants to play in single or multiplayer mode.
* User is given a choice of playing first or second and also the piece that he wants.
* Once the game starts, the user can enter his input in the squares which are
0 indexed in the matrix of squares. So if the user wants to input in the top left of
the board, he has to enter "00".
* The entries in the board are actually stored in 1D array where the indexes are mapped
to a dictionary of user inputs.
* When the computer turn comes, it uses MiniMax algorithm which finds the best move
in the given position.
* The MiniMax is implemented using backtracking where the computer calculates 
all possible moves and assigns weight to each series of move performed. Weight of each move is calcuated by the square of previous move. The square index is tracked each time the algorithm finds the best move so far.
* The move with maximum value for the computer is chosen.
* The board is checked in each iteration to see if we have a winner or not. All possible
winning combinations are tracked in an array. If we already have a winner, 
the loop is broken and the winner is printed back to the console.

## Running the code
> python tic_tac_mm.py <br />

* You will get user inputs of selecting the type of game mode (Single or Multiplayer)
* User is provided another user input of chosing the type of piece.
* In front the computer, the user has a choice of playing first or second.
* Result of the game is shown in the end of the program.

## Results
The screenshots of the results are in the results folder in this git.



 