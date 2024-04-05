

import random


class Ai():
    def __init__(self):
        empty=[]
        self.strike_queue = empty[:]
        self.checked=empty[:]

    def strike(self,difficulty, strike_board):
        '''
            returns a tuple of coordinates to strike
        '''
        match difficulty:
            case "Easy":
                return self.easy_strike(strike_board)
            case "Medium":
                return self.medium_strike(strike_board)
            case "Hard":
                return self.hard_strike(strike_board)



    def easy_strike(self,strike_board):
        '''
            returns a random tuple of coordinates to strike
        '''
        valid_strikes=[]
        for i in range(10):
            for j in range(10):
                if strike_board.get_simbol(i,j)==None:
                    valid_strikes.append((i,j))

        return random.choice(valid_strikes)

    def medium_strike(self,strike_board):
        '''
            returns a tuple of coordinates to strike
        '''
        valid_strikes=[]
        missed_strikes=[]
        hit_strikes=[]
        for i in range(10):
            for j in range(10):
                if strike_board.get_simbol(i,j)==None:
                    valid_strikes.append((i,j))
                elif strike_board.get_simbol(i,j)=='X' and (i,j) not in self.checked:
                    hit_strikes.append((i,j))
                elif strike_board.get_simbol(i,j)=='-':
                    missed_strikes.append((i,j))
                    
        if len(hit_strikes)==0 and len(self.strike_queue)==0:
            self.strike_queue.append(random.choice(valid_strikes))

        if len(hit_strikes)==1:
            x,y=hit_strikes[0]
            self.checked.append((x,y))
            if x+1 <= 9 and strike_board.get_simbol(x+1,y)==None:
                self.strike_queue.append((x+1,y))
            if x-1 >= 0 and strike_board.get_simbol(x-1,y)==None:
                self.strike_queue.append((x-1,y))
            if y+1 <= 9 and strike_board.get_simbol(x,y+1)==None:
                self.strike_queue.append((x,y+1))
            if y-1 >= 0 and strike_board.get_simbol(x,y-1)==None:
                self.strike_queue.append((x,y-1))

        if len(hit_strikes)>1:
            x,y=hit_strikes[0]
            self.checked.append((x,y))
            if x+1 <= 9 and strike_board.get_simbol(x+1,y)==None:
                self.strike_queue.append((x+1,y))
            if x-1 >= 0 and strike_board.get_simbol(x-1,y)==None:
                self.strike_queue.append((x-1,y))
            if y+1 <= 9 and strike_board.get_simbol(x,y+1)==None:
                self.strike_queue.append((x,y+1))
            if y-1 >= 0 and strike_board.get_simbol(x,y-1)==None:
                self.strike_queue.append((x,y-1)) 


        if len(self.strike_queue)==0:
            self.strike_queue.append(random.choice(valid_strikes))

        test= self.strike_queue
        return self.strike_queue.pop(0)


    def hard_strike(self,strike_board):
        '''
            returns a tuple of coordinates to strike
        '''
        valid_strikes=[]
        missed_strikes=[]
        hit_strikes=[]
        for i in range(10):
            for j in range(10):
                if strike_board.get_simbol(i,j)==None:
                    valid_strikes.append((i,j))
                elif strike_board.get_simbol(i,j)=='X':
                    hit_strikes.append((i,j))
                elif strike_board.get_simbol(i,j)=='-':
                    missed_strikes.append((i,j))
        if len(hit_strikes)==0 and len(self.strike_queue)==0:
            self.strike_queue.append(random.choice(valid_strikes))
        
        if len(hit_strikes)==1:
            x,y=hit_strikes[0]
            if strike_board.get_simbol(x+1,y)==None:
                self.strike_queue.append((x+1,y))
            if strike_board.get_simbol(x-1,y)==None:
                self.strike_queue.append((x-1,y))
            if strike_board.get_simbol(x,y+1)==None:
                self.strike_queue.append((x,y+1))
            if strike_board.get_simbol(x,y-1)==None:
                self.strike_queue.append((x,y-1))

        if len(hit_strikes)>1:
            for i in range(0,len(hit_strikes)):
                if hit_strikes[i] not in self.checked:
                    x,y=hit_strikes[i]
                    if x+1 <= 9 and strike_board.get_simbol(x+1,y)==None and (x,y) not in self.strike_queue:
                        self.strike_queue.append((x+1,y))
                    if x-1 >= 0 and strike_board.get_simbol(x-1,y)==None and (x,y) not in self.strike_queue:
                        self.strike_queue.append((x-1,y))
                    if y+1 <= 0 and strike_board.get_simbol(x,y+1)==None and (x,y) not in self.strike_queue:
                        self.strike_queue.append((x,y+1))
                    if y-1 <= 0 and strike_board.get_simbol(x,y-1)==None and (x,y) not in self.strike_queue:
                        self.strike_queue.append((x,y-1))
            pass
        if len(self.strike_queue)==0:
            self.strike_queue.append(random.choice(valid_strikes))


        return self.strike_queue.pop(0)
            


        #TODO: implement hard strike
        #try to place strikes near the last hit
        #try to build a plane from the hits
        #try to use the missed strikes as well
        