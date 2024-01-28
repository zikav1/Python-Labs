import tkinter


class TicTacToeBoard:
    #Skapar ett Tre-i-rad-bräde med alla platser lediga från början.
    #Raderna och kolumnerna går från 0 till 2.
    def __init__(self):
        self.restart()
    

    #Returnerar värdet på plats row, col. Returvärdet är antingen
    #'X', 'O', eller '-' för en ledig plats.
    #row och col antas vara mellan 0 och 2.
    def get(self,row,col):
        return self._board[row][col]

    
    #Returnerar True om platsen row, col är ledig, annars False.
    #row och col antas vara mellan 0 och 2.
    def is_empty(self,row,col):
        if self._board[row][col] == '-':
            return True
        else:
            return False


    #Försöker placera markören marker på platsen row, col. Detta sker
    #om platsen är ledig och markören är antingen 'X' eller 'O'.
    #Returnerar True om så är fallet, annars False.
    #row och col antas vara mellan 0 och 2.
    def place(self, marker, row, col):
        if (self.is_empty(row,col)) and (marker == 'X' or marker == 'O'):
            self._board[row][col] = marker
            return True
        else:
            return False


    #Skriver ut brädet enligt följande formattering:
    #X O -
    #X X O
    #O - X
    def print_board(self):
        for row in range (len(self._board)):
            for col in range (len(self._board[row])):
                print(self._board[row][col],end = ' ')
            print(' ')

    #Returnerar True om brädet är fullt, annars False.
    def is_full(self):
        
        full = False
        for row in range (len(self._board)):
            for col in range (len(self._board[row])):
                if self._board[row][col] == 'X' or self._board[row][col] == 'O':
                    full = True
                else:
                    full = False
        return full
    
    #Nollställer brädet. Alla platser blir lediga.
    def restart(self):
        self._board = [['-' for _ in range(3)] for _ in range(3)]

    #Returnerar True om markören marker har vunnit, annars False.
    def is_winner(self, marker):
        
        for row in self._board:
            if all(cell == marker for cell in row):
                return True
        for column in range(3):
            if all(row[column] == marker for row in self._board):
                return True
        if self._board[0][0] == self._board[1][1] == self._board[2][2] == marker:
                return True
        if self._board[0][2] == self._board[1][1] == self._board[2][0] == marker:
            return True
        
        return False





board = TicTacToeBoard()
board.restart()






