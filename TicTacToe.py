from pynput import keyboard
import os
import time
import math
from sys import platform
class Board():
    def __init__(self) -> None:
        self.dim = 3
        self.board = [[' . ', ' . ', ' . '] for _ in range(self.dim)]
    

    ####SHOW BOARD
    def show(self):
        

        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        for i in self.board:
            for j in i:
                print(j,end='')
            print('')


    ###CLEAR BOARD
    def clear(self):
        self.board = [[' . ', ' . ', ' . '] for i in range(self.dim)]

    
    ###CHECKS IF 'X' OR 'O' CAN BE PLACED
    def is_valid(self, row,col):
        return self.board[row][col] != ' x ' and self.board[row][col] != ' o '
    
    
    ####PLACE SYMBOL ON ROW, COL
    def place(self, row, col, char):
        if self.is_valid(row,col):
            self.board[row][col] = char
        self.show()
    
    ####GET ROW AND COL BY PLACE_NUMBER
    def get_row_col(self, key):
        row = (key-1) // 3
        col = (key+2) % 3 
        return (row, col)
    
    ###GET EMPTY CELLS
    def get_empty(self):
        cells = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' . ':
                    cells.append((i,j))
        return cells


    ###CHECK WIN
    def win(self):
        ###Check cols
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != ' . ':
                return self.board[0][i]


        ###Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != ' . ':
                return self.board[i][0]


        ###Chek diag
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] != ' . ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[1][1] != ' . ':
            return self.board[0][2]
        
        return False


    ###CHECK TIE
    def tie(self):
        if not self.win():
            for i in self.board:
                if ' . ' in i: return False
            return True
        return False
    
    
        



class Players():
    def __init__(self) -> None:
        self.char = {
            1: ' x ',
            -1: ' o '
        }
        self.first = ' x '
        self.second = ' o '
        self.curr = 1 # 1 if next - first,      -1 if next - second
    






class TicTacToe():
    def __init__(self) -> None:
        self.board = Board()
        self.players = Players()
        
    

    def get_key(self):
        if platform == "win32":
            try:
                return int(keyboard.read_key(suppress=True))  
            except:
                self.get_key()
        else:

            self.t = False
            def on_press(key):
                
                if key == keyboard.Key.esc:
                    # Stop listener
                    return False
                    
            def on_release(key):
                try:
                    self.t = int(key.char)
                    return False
                except:
                    pass
            listener = keyboard.Listener(
                on_press=on_press,
                on_release=on_release)
            listener.start()
            while True:
                if self.t:
                    return self.t
            
            
        

    def input_key(self):
        try:
            return int(input('Write value from 1 to 9: '))
        except:
            self.input_key()
    


    def menu(self):
        if platform == "win32":
            os.system('cls')
        else:
            os.system('clear')
        print('Welcome to Tic-Tac-Toe game!')
        print('1 - VS Bot')
        print('2 - 2 Players')
        print('3 - Explanation')
        print('4 - Exit')

        key = self.get_key()

        if key == 1:
            self.start_bot()
        elif key == 2:
            self.start_players()
        elif key == 3:
            self.explanation()
        elif key == 4:
            exit()
        else:
            self.menu()
        


    #################EXPLANATION 
    def expl_fill(self):
        ###IF FILLED ALL GAPS
        if self.board.board == [[' . ', ' . ', ' . '] for i in range(3)]:
            self.menu()
        time.sleep(0.1)
        key = self.get_key()
        row, col = self.board.get_row_col(key)
        self.board.place(row, col, ' . ')
        self.expl_fill()

    def expl_place(self, row, col):
        self.board.board[row][col] = ' . '
        self.board.show()

    def explanation(self):
        ###SET BOARD TO 
        # 1 2 3
        # 4 5 6
        # 7 8 9
        self.board.board = [[' '+str(1 + 3*(i-1))+' ',' '+str(1 + 3*(i-1)+1)+' ',' '+str(1 + 3*(i-1)+2)+' '] for i in range(1,4)]
        self.board.show()
        print()
        print('Press number to put . on this place')
        print('Fill all the gaps to continue')
        self.expl_fill()




    ##################2 PLAYERS GAME
    def start_players(self):
        self.board.show()
        if self.players.curr == 1:
            print('X\'s turn')
        else:
            print('O\'s turn')
        time.sleep(0.1)
        key = self.get_key()
        row, col = self.board.get_row_col(key)
        if self.board.is_valid(row,col):
            self.board.place(row,col,self.players.char[self.players.curr])
        else:
            self.start_players()
        self.players.curr *= -1
        if winner:=self.board.win():
            if platform == "win32":
                os.system('cls')
            else:
                os.system('clear')
            print(str(winner).upper()+'winns!!!')
            input('Press Enter to continue.')
            self.board.clear()
            self.players.curr = 1
            self.menu()
        if self.board.tie():
            if platform == "win32":
                os.system('cls')
            else:
                os.system('clear')
            print('Tie!!!')
            input('Press Enter to continue.')
            self.board.clear()
            self.players.curr = 1
            self.menu()
        self.start_players()

        

        
        


    
    ###### VS BOT
    def start_bot(self):
        self.board.show()
        if self.players.curr == 1:
            print('Your turn')
            time.sleep(0.1)
            key = self.get_key()
            row, col = self.board.get_row_col(key)
            if self.board.is_valid(row,col):
                self.board.place(row,col,self.players.char[self.players.curr])
            else:
                self.start_bot()
            self.players.curr *= -1
        else:
            r, c, _ = self.minimax(self.board, -1)
            self.board.place(r, c, self.players.char[self.players.curr])
            self.players.curr *= -1

        if winner:=self.board.win():
            print(str(winner).upper()+'winns!!!')
            input('Press Enter to continue.')
            self.board.clear()
            self.players.curr = 1
            self.menu()

        if self.board.tie():
            print('Tie!!!')
            input('Press Enter to continue.')
            self.board.clear()
            self.players.curr = 1
            self.menu()
        self.start_bot()
    

    ###ALGORITHM TO FIND THE BEST MOVE FOR BOT
    def minimax(self, board: Board, player):
        if player == -1:
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, math.inf]
        
        if winner:=board.win(): 
            if winner == ' x ': return [-1,-1, -1] 
            elif winner == ' o ': return [-1,-1, +1]
        elif board.tie(): return [-1,-1,0]

        for cell in board.get_empty():
            r, c = cell
            board.board[r][c] = ' o ' if player == -1 else ' x '
            score = self.minimax(board, -player)
            board.board[r][c] = ' . '
            score[0], score[1] = r, c

            if player == -1:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
        
        return best
