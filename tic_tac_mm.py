class TicTacToe:
    def __init__(self, singleOrMulti, player1, player2, player1_piece, player2_piece, turn) -> None:
        self.moves = [0 for _ in range(0,9)]
        self.wining_combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.move_map = {"00":0, "01": 1, "02": 2, "10": 3, "11": 4, "12": 5, "20": 6, "21": 7, "22":8}
        self.turn = turn
        self.player1 = player1
        self.player2 = player2
        self.player1_piece = player1_piece
        self.player2_piece = player2_piece
        self.singleOrMulti = singleOrMulti


    def play(self):
        status = -1
        if self.singleOrMulti == 1:
            for i in range(0,9):
                self.printing_board()
                status = self.check_for_win()
                if(status != -1):
                    break
                if (i+self.turn)%2 == 0:
                    self.computer_playing()
                else:
                    self.player_playing(1)
        else:
            for i in range(0,9):
                self.printing_board()
                status = self.check_for_win()
                if(status != -1):
                    break
                if i%2 == 0:
                    self.player_playing(1)
                else:
                    self.player_playing(2)

        if status == -1:
            print("Game is drawn....")
        elif status == 1:
            print("Game won by player 1")
        elif status == 2:
            print("Game won by player 2")

    def check_for_win(self):
        for i in range(len(self.wining_combos)):
            if self.moves[self.wining_combos[i][0]] != 0 and (self.moves[self.wining_combos[i][0]] == self.moves[self.wining_combos[i][1]] == self.moves[self.wining_combos[i][2]]):
                return self.moves[self.wining_combos[i][0]]
        
        return -1

    def minimax(self, player):
        status=self.check_for_win();
        if(status!=-1):
            return (status*player);
        pos=-1;
        value=-2;
        for i in range(0,9):
            if(self.moves[i]==0):
                self.moves[i]=player;
                score=-self.minimax((player*-1));
                if(score>value):
                    value=score;
                    pos=i;
                self.moves[i]=0;

        if(pos==-1):
            return 0;
        return value;
        
    #This function makes the computer's move using minmax algorithm.
    def computer_playing(self):
        pos=-1;
        value=-2;
        for i in range(0,9):
            if(self.moves[i]==0):
                self.moves[i]=1;
                score=-self.minimax(-1);
                self.moves[i]=0;
                if(score>value):
                    value=score;
                    pos=i;
    
        self.moves[pos]=2;

    def player_playing(self, player):
        stringmove = input("Enter player move in terms of row and column where first row and column is 0: ")
        if stringmove not in self.move_map:
            print("Entered move is wrong. Enter as 11 if you want to place piece on 1st row and first column")
            exit(1)
        player_move = self.move_map[stringmove]

        if self.moves[player_move] != 0:
            print("Entered move which was already done. Please insert the piece in empty place.")
            exit(1)

        self.moves[player_move] = player

    def printing_board(self):
        print("Current State Of Board : \n\n");
        for i in range (0,9):
            if((i>0) and (i%3)==0):
                print("\n");
            if(self.moves[i]==0):
                print("- ",end=" ");
            if (self.moves[i]==1):
                print(self.player1_piece + " ",end=" ");
            if(self.moves[i]==2):    
                print(self.player2_piece + " ",end=" ");
        print("\n\n")

if __name__ == "__main__" :
    singleOrMulti = int(input("Enter 1 for single player and 2 for multiplayer: "))

    if singleOrMulti == 1:
        piece_choice = input("Enter '0' or 'X' for your piece choice: ")
        player1_piece = piece_choice
        if(piece_choice == "0"):
            player2_piece = "X"
            print("Computer piece is: X")
        elif(piece_choice == "X"):
            player2_piece = "0"
            print("Computer piece is: 0")
        else:
            print("Invalid input for selecting piece. Try Again.")
            exit(1)
        turn = int(input("Enter 1 to play first or 2 to play second: "))
        
        tictac = TicTacToe(singleOrMulti,1, -1, player1_piece, player2_piece, turn)

    elif singleOrMulti == 2:
        piece_choice = input("Enter '0' or 'X' for your player 1 piece choice: ")
        player1_piece = piece_choice
        if(piece_choice == "0"):
            player2_piece = "X"
            print("Player 2 piece is: X")
        elif(piece_choice == "X"):
            player2_piece = "0"
            print("Player 2 piece is: 0")
        else:
            print("Invalid input for selecting piece. Try Again.")
            exit(1)
        turn = int(input("Enter 1 to play first or 2 to play second: "))
        tictac = TicTacToe(singleOrMulti,1, 2, player1_piece, player2_piece, turn)
    else:
        print("Invalid input for single and multiplayer.")
        exit(1)

    tictac.play()

    
    
    