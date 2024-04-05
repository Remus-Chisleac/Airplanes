
import random
import sys
from pathlib import Path

path=Path().parent.absolute()
sys.path.insert(0, str(path))

from src.domain.Board import Board
from src.domain.Planes import Planes
from src.AI.ai import Ai


class Settings():
    def __init__(self):
        self.poz = [0,0,1,1]
        self.__tutorial = ["On", "Off"]
        self.__difficulty = ["Easy", "Medium", "Hard"]
        self.__downed_plane = ["Reveal_full", "Reveal_head", "Off"]
        self.__second_wind = ["On", "Off"]



    @property
    def tutorial(self):
        return self.__tutorial[self.poz[0]]

    @property
    def difficulty(self):
        return self.__difficulty[self.poz[1]]

    @property
    def downed_plane(self):
        return self.__downed_plane[self.poz[2]]

    @property
    def second_wind(self):
        return self.__second_wind[self.poz[3]]


    def add_tutorial(self):
        self.poz[0] = self.poz[0]+1
        if self.poz[0] == 2:
            self.poz[0] = 0

    def sub_tutorial(self):
        self.poz[0] = self.poz[0]-1
        if self.poz[0] == -1:
            self.poz[0] = 1

    def add_difficulty(self):
        self.poz[1] = self.poz[1]+1
        if self.poz[1] == 3:
            self.poz[1] = 0

    def sub_difficulty(self):
        self.poz[1] = self.poz[1]-1
        if self.poz[1] == -1:
            self.poz[1] = 2
    
    def add_downed_plane(self):
        self.poz[2] = self.poz[2]+1
        if self.poz[2] == 3:
            self.poz[2] = 0
    
    def sub_downed_plane(self):
        self.poz[2] = self.poz[2]-1
        if self.poz[2] == -1:
            self.poz[2] = 2

    def add_second_wind(self):
        self.poz[3] = self.poz[3]+1
        if self.poz[3] == 2:
            self.poz[3] = 0
    
    def sub_second_wind(self):
        self.poz[3] = self.poz[3]-1
        if self.poz[3] == -1:
            self.poz[3] = 1



class Game_services():
    def __init__(self,user_board,user_strikes,computer_board,computer_strikes,repo):
        self.__user_board = user_board
        self.__user_strikes = user_strikes
        self.__user_planes = []
        self.__computer_board = computer_board
        self.__computer_strikes = computer_strikes
        self.__computer_planes = []
        self.__repo=repo
        self.__ai=Ai()


    def new_game(self):
        __user_board = Board()
        __user_strikes = Board()
        lis=[]
        __user_planes = lis[:]
        __computer_board = Board()
        __computer_strikes = Board()
        __computer_planes = lis[:]

    @property
    def user_board(self):
        return self.__user_board
    
    @property
    def user_strikes(self):
        return self.__user_strikes
    
    @property
    def computer_board(self):
        return self.__computer_board
    
    @property
    def computer_strikes(self):
        return self.__computer_strikes

    @property
    def user_planes(self):
        return self.__user_planes
    
    @property
    def computer_planes(self):
        return self.__computer_planes

    def reset(self):
        '''
            resets the game board and lists
        '''
        self.__user_board = Board()
        self.__user_board.reset_board()
        self.__user_strikes = Board()
        self.__user_strikes.reset_board()
        lis=[]
        self.__user_planes = lis[:]
        self.__computer_board = Board()
        self.__computer_board.reset_board()
        self.__computer_strikes = Board()
        self.__computer_strikes.reset_board()
        self.__computer_planes = lis[:]


    def add_plane(self,pozx,pozy,orientation,board,planes):
        '''
            function to add a plane on the board
        :param:
            pozx - board coord
            pozy - board coord
            orientation - plane orientation
            planes - list of planes on the board [x](head coords) [x+1](top right corner, orienattion)
        '''
        match orientation:
            case 0:
                x,y,plane=Planes().plane_nord()
            case 1:
                x,y,plane=Planes().plane_east()
            case 2:
                x,y,plane=Planes().plane_south()
            case 3:
                x,y,plane=Planes().plane_west()
            case _: 
                x,y,plane=Planes().plane_nord()  

        _board=board.get_board()
        for i in range(len(plane)):
            for j in range(len(plane[i])):
                if plane[i][j] != ' ' and _board[pozy+i][pozx+j]!=' ':
                    return False

        for i in range(len(plane)):
            for j in range(len(plane[i])):
                if plane[i][j] != " ":
                    board.place_simbol(pozy+i,pozx+j,plane[i][j])
        planes.append([pozx+x,pozy+y])
        planes.append([pozx,pozy,orientation])
        return True


    def verif_plane(self,pozx,pozy,orientation,board):
        '''
            verifies if a plane can fit in a board
        
        :param:
            pozx - board coord
            pozy - board coord
            orientation - plane orientation(N/E/S/W)
            board - board the stores the planes
        '''
        match orientation:
            case 0:
                x,y,plane=Planes().plane_nord()
            case 1:
                x,y,plane=Planes().plane_east()
            case 2:
                x,y,plane=Planes().plane_south()
            case 3:
                x,y,plane=Planes().plane_west()
            case _: 
                x,y,plane=Planes().plane_nord()  

        _board=board.get_board()
        if pozy+len(plane)>10 or pozx+len(plane[0])>10:
            return False
        for i in range(len(plane)):
            for j in range(len(plane[i])):
                if plane[i][j] != ' ' and _board[pozy+i][pozx+j]!=' ':
                    return False
        return True


    def ai_add_plane(self):
        '''
            function to plce the computer`s planes
        '''
        cnt=0
        while True:
            pozx = random.randint(0,9)
            pozy = random.randint(0,9)
            orientation = random.randint(0,3)
            match orientation:
                case 0:
                    x,y,plane=Planes().plane_nord()
                case 1:
                    x,y,plane=Planes().plane_east()
                case 2:
                    x,y,plane=Planes().plane_south()
                case 3:
                    x,y,plane=Planes().plane_west()
                case _: 
                    x,y,plane=Planes().plane_nord()  
            if pozy+len(plane)<=10 and pozx+len(plane[0])<=10:
                if self.verif_plane(pozx,pozy,orientation,self.__computer_board):
                    if self.add_plane(pozx,pozy,orientation,self.__computer_board,self.__computer_planes):
                        cnt+=1
                        if cnt==3:
                            break
    

    def strike(self,x,y,plane_board,strike_board):
        '''
            function to proces strikes
        
        :param:
            x - board coord
            y - board coord
            plane_board - board that holds the planes
            strike_board - board that holds the strikes
        :return:
            kind of strike
                False - invalid strike
                Miss
                Head - Head strike
                Body - Body strike
        '''
        if plane_board.get_simbol(y,x) == '-':
            return False
        if plane_board.get_simbol(y,x) == None:
            strike_board.place_simbol(y,x,'-')
            return "Miss"
        else:
            strike_board.place_simbol(y,x,'X')
            if plane_board.get_simbol(y,x) == 'H':
                return "Head"
            if plane_board.get_simbol(y,x) == 'B':
                return "Body"
            


    def computer_strike(self,difficulty):
        '''
            function to get and execute the computers strike
        :param:
            difficulty - ai level
        :return:
            resault of strike
        '''
        x,y = self.__ai.strike(difficulty,self.__computer_strikes)
        hit = self.strike(x,y,self.__user_board,self.__computer_strikes)
        
        return hit,x,y
        



    def reveal_plane(self,head_x,head_y,strike_board,planes):
        '''
            function to reveal the plane by hiting all of its parts
        :param:
            head_x - board coord for the head of the plane
            head_y - board coord for the head of the plane
            strike_board - board of strikes
            planes - list of planes on the board [x](head coords) [x+1](top right corner, orienattion)
        '''
        index=planes.index([head_x,head_y])+1
        pozx,pozy,orientation=planes[index]
        match orientation:
            case 0:
                x,y,plane=Planes().plane_nord()
            case 1:
                x,y,plane=Planes().plane_east()
            case 2:
                x,y,plane=Planes().plane_south()
            case 3:
                x,y,plane=Planes().plane_west()
            case _:
                x,y,plane=Planes().plane_nord()
        for i in range(len(plane)):
            for j in range(len(plane[i])):
                if plane[i][j] != ' ':
                    strike_board.place_simbol(pozy+i,pozx+j,'X')

        pass
        

        

    
