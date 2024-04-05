
# Description: This class is used to create a board object
class Board():
    '''
        game board used to store planes and strikes
    '''
    def __init__(self):
        self.__board =[]
        for i in range(10):
            self.__board.append([' ']*10)

    def get_board(self):
        return self.__board[:]

    def set_board(self, board):
        self.__board = board[:]
    
    def reset_board(self):
        self.__board =[]
        for i in range(10):
            self.__board.append([' ']*10)

    def place_simbol(self, x, y, simbol):
        self.__board[x][y] = simbol

    def remove_simbol(self, x, y):
        self.__board[x][y] = ' '

    def get_simbol(self, x, y):
        if self.__board[x][y]!=' ':
            return self.__board[x][y] 
        else: 
            return None

    def __str__(self):
        return str(self.__board)
        
    def __repr__(self):
        return "Board("+str(self.__board)+")"
    
    

    

    