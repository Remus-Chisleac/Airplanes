import os
import time
import keyboard as kb
import sys
from pathlib import Path

path=Path().parent.absolute()
sys.path.insert(0, str(path))

from src.services.Game_services import Game_services, Settings
from src.domain.Planes import Planes

class UI():
    def __init__(self, service, settings):
        self.__settings=settings
        self.__service = service
        self.__continue= False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


    def __ingame(self):
        reveal_plane = self.__settings.downed_plane
        line_sep ="+---+---+---+---+---+---+---+---+---+---+"
        line_vert="| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |"
        table_sep=  "            "
        end ='\n'
        cursor_posx =0
        cursor_posy =0
        last_strike=False

        user_nr_planes=3
        computer_nr_planes=3
        while True:
            self.clear()
            display_board=[]
            plane_board=self.__service.user_board.get_board()
            strike_board=self.__service.user_strikes.get_board()
            computer_strikes=self.__service.computer_strikes.get_board()

            for i in range(0,10):
                for j in range(0,10):
                    if computer_strikes[i][j] != ' ':
                        plane_board[i][j]=computer_strikes[i][j]
            k=-1
            for i in range(0,10):
                k+=1
                display_board.append("")
                display_board[k]+=line_sep
                display_board[k]+=table_sep
                display_board[k]+=line_sep
                display_board[k]+=end
                k+=1
                display_board.append("")
                display_board[k]+=line_vert.format(*strike_board[i])
                display_board[k]+=table_sep
                display_board[k]+=line_vert.format(*plane_board[i])
                display_board[k]+=end
            k+=1
            display_board.append("")
            display_board[k]+=line_sep
            display_board[k]+=table_sep
            display_board[k]+=line_sep
            display_board[k]+=end

            screen_pos_x = cursor_posx*4+2
            screen_pos_y = cursor_posy*2+1

            display_board[screen_pos_y-1]=list(display_board[screen_pos_y-1])
            display_board[screen_pos_y]=list(display_board[screen_pos_y])
            display_board[screen_pos_y+1]=list(display_board[screen_pos_y+1])


            display_board[screen_pos_y-1][screen_pos_x-2]='╔'
            display_board[screen_pos_y-1][screen_pos_x+2]='╗'
            display_board[screen_pos_y+1][screen_pos_x-2]='╚'
            display_board[screen_pos_y+1][screen_pos_x+2]='╝'
            display_board[screen_pos_y][screen_pos_x-2]='║'
            display_board[screen_pos_y][screen_pos_x+2]='║'
            display_board[screen_pos_y-1][screen_pos_x-1]='═'
            display_board[screen_pos_y-1][screen_pos_x]='═'
            display_board[screen_pos_y-1][screen_pos_x+1]='═'
            display_board[screen_pos_y+1][screen_pos_x-1]='═'
            display_board[screen_pos_y+1][screen_pos_x]='═'
            display_board[screen_pos_y+1][screen_pos_x+1]='═'

            display_board[screen_pos_y-1]=''.join(display_board[screen_pos_y-1])
            display_board[screen_pos_y]=''.join(display_board[screen_pos_y])
            display_board[screen_pos_y+1]=''.join(display_board[screen_pos_y+1])

            



            for i in range(len(display_board)):
                print(display_board[i],end="")
            print()
            print()

            print("x:",cursor_posx,"|y:",cursor_posy)
            print("use the arrow keys to move the pointer")
            print("use enter to confirm the strike")
            


            
            key = kb.read_event()
            if key.event_type == "down":
                key= key.name
                match key:
                    case "up":
                        cursor_posy-=1
                        if cursor_posy == -1:
                            cursor_posy = 9
                    case "down":
                        cursor_posy+=1
                        if cursor_posy == 10:
                            cursor_posy = 0

                    case "left":
                        cursor_posx-=1
                        if cursor_posx == -1:
                            cursor_posx = 9
                    case "right":
                        cursor_posx+=1
                        if cursor_posx == 10:
                            cursor_posx = 0

                    case "enter":
                        
                        if self.__service.user_strikes.get_board()[cursor_posy][cursor_posx] == " ":
                            hit = self.__service.strike(cursor_posx,cursor_posy,self.__service.computer_board,self.__service.user_strikes)
                            match reveal_plane:
                                case "Reveal_full":
                                    if hit == "Head":
                                        self.__service.reveal_plane(cursor_posx,cursor_posy,self.__service.user_strikes\
                                            ,self.__service.computer_planes)
                                        print("Enemy plane destroyed")
                                        time.sleep(1)

                                    pass
                                case "Reveal_head":
                                    if hit == "Head":
                                        print("Enemy plane destroyed")
                                        time.sleep(1)
                                    pass
                                case "Off":

                                    pass
                            if hit == "Head":
                                user_nr_planes-=1
                                if user_nr_planes ==0:
                                    if self.__settings.second_wind == "Off":

                                        
                                        print("=====================================")
                                        print("|            Human wins             |")
                                        print("=====================================")
                                        input()
                                        time.sleep(5)
                                    else:
                                        hit = self.__service.computer_strike(self.__settings.difficulty)
                                        if hit == "Head":
                                            computer_nr_planes-=1
                                            if computer_nr_planes ==0:
                                                
                                                print("=====================================")
                                                print("|               Drow                |")
                                                print("=====================================")
                                                input()
                                                time.sleep(5)
                                    return
                            if last_strike ==True:
                                
                                print("=====================================")
                                print("|           Computer wins           |")
                                print("=====================================")
                                input()
                                time.sleep(5)

                                pass
                            hit,x,y = self.__service.computer_strike(self.__settings.difficulty)
                            match reveal_plane:
                                case "Reveal_full":
                                    if hit == "Head":
                                        self.__service.reveal_plane(x,y,self.__service.computer_strikes\
                                            ,self.__service.user_planes)
                                        print("Ally plane destroyed")
                                        time.sleep(1)

                                    pass
                                case "Reveal_head":
                                    if hit == "Head":
                                        print("Ally plane destroyed")
                                        time.sleep(1)
                                    pass
                                case "Off":
                                    if hit == "Head":
                                        print("Ally plane destroyed")
                                        time.sleep(1)
                                    pass
                            if hit == "Head":
                                computer_nr_planes-=1
                                if computer_nr_planes ==0:
                                    if self.__settings.second_wind == "Off":
                                        
                                        print("=====================================")
                                        print("|           Computer wins           |")
                                        print("=====================================")
                                        input()
                                        time.sleep(5)
                                    else:
                                        self.clear()
                                        print("Second_wind")
                                        last_strike=True
                                        time.sleep(5)
                                    return
                        else:
                            print("You already shot here")
                            time.sleep(1)
                    case "esc":
                        return

        pass



    def __settings_menu(self):
        cursor = ">"
        cursor_pos = 0
        empty = " "
        menu=["Tutorial","Difficulty","Downed_plane","Second_wind","Back"]
        while True:
            values = [self.__settings.tutorial,self.__settings.difficulty,self.__settings.downed_plane,self.__settings.second_wind]
            self.clear()
            print("======Settings======")
            for i in range(len(menu)):
                if i == cursor_pos:
                    print(cursor,menu[i],end="")
                else:
                    print(empty,menu[i],end="")
                if i != len(menu)-1:
                    print(" | ",values[i])
            
            key =kb.read_event()
            if key.event_type == "down":
                key = key.name
                match key:
                    case "up":
                        cursor_pos-=1
                        if cursor_pos == -1:
                            cursor_pos = len(menu)-1
                    case "down":
                        cursor_pos+=1
                        if cursor_pos == len(menu):
                            cursor_pos = 0
                    case "left":
                        match cursor_pos:
                            case 0:
                                self.__settings.sub_tutorial()
                            case 1:
                                self.__settings.sub_difficulty()
                            case 2:
                                self.__settings.sub_downed_plane()
                            case 3:
                                self.__settings.sub_second_wind()
                    case "right":
                        match cursor_pos:
                            case 0:
                                self.__settings.add_tutorial()
                            case 1:
                                self.__settings.add_difficulty()
                            case 2:
                                self.__settings.add_downed_plane()
                            case 3:
                                self.__settings.add_second_wind()
                    case "enter":
                        match cursor_pos:
                            case 4:
                                break
                    case "esc":
                        break


            

    def __new_game(self):
        line_sep ="+---+---+---+---+---+---+---+---+---+---+"
        line_vert="| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |"
        cursor_posx = 0
        cursor_posy = 0
        orientation = 0
        placed_planes = 0
        while True:
            self.clear()
            print("======New Game======")
            print()

            self.__service.new_game()
            print("Place {} planes".format(3-placed_planes))

            display_board=[]
            plane_board=self.__service.user_board.get_board()
            k=-1
            for i in range(len(plane_board)):
                k+=1
                display_board.append('')
                display_board[k]+=line_sep

                k+=1
                display_board.append('')
                display_board[k]+=line_vert.format(*plane_board[i])
            k+=1
            display_board.append('')
            display_board[k]+=line_sep

            screen_pos_x = cursor_posx*4+2
            screen_pos_y = cursor_posy*2+1

            for i in range(0,len(display_board)):
                display_board[i]=list(display_board[i])


            display_board[screen_pos_y-1][screen_pos_x-2]='╔'
            display_board[screen_pos_y-1][screen_pos_x+2]='╗'
            display_board[screen_pos_y+1][screen_pos_x-2]='╚'
            display_board[screen_pos_y+1][screen_pos_x+2]='╝'
            display_board[screen_pos_y][screen_pos_x-2]='║'
            display_board[screen_pos_y][screen_pos_x+2]='║'
            display_board[screen_pos_y-1][screen_pos_x-1]='═'
            display_board[screen_pos_y-1][screen_pos_x]='═'
            display_board[screen_pos_y-1][screen_pos_x+1]='═'
            display_board[screen_pos_y+1][screen_pos_x-1]='═'
            display_board[screen_pos_y+1][screen_pos_x]='═'
            display_board[screen_pos_y+1][screen_pos_x+1]='═'

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

            valid_plane=False
            if cursor_posx + len(plane[0])-1 <= 10 and cursor_posy + len(plane)-1 <= 10 and self.__service.verif_plane(cursor_posx,cursor_posy,orientation,self.__service.user_board):
                valid_plane=True
                offset_x = screen_pos_x
                offset_y = screen_pos_y
                for i in range(len(plane)):
                    for j in range(len(plane[i])):
                        if plane[i][j] != " ":
                            display_board[offset_y][offset_x]=plane[i][j]
                        offset_x+=4
                    offset_x = screen_pos_x
                    offset_y+=2

            for i in range(0,len(display_board)):
                display_board[i]=''.join(display_board[i])
                print(display_board[i])

            key = kb.read_event()
            if key.event_type == "down":
                key = key.name
                match key:
                    case "up":
                        cursor_posy-=1
                        if cursor_posy == -1:
                            cursor_posy = 9
                    case "down":
                        cursor_posy+=1
                        if cursor_posy == 10:
                            cursor_posy = 0
                    case "left":
                        cursor_posx-=1
                        if cursor_posx == -1:
                            cursor_posx = 9
                    case "right":
                        cursor_posx+=1
                        if cursor_posx == 10:
                            cursor_posx = 0
                    case "q":
                        orientation-=1
                        if orientation == -1:
                            orientation = 3
                    case "e":
                        orientation+=1
                        if orientation == 4:
                            orientation = 0
                    case "esc":
                        self.__service.reset()
                        break
                    case "enter":
                        if valid_plane:
                            if self.__service.add_plane(cursor_posx,cursor_posy,orientation,self.__service.user_board,self.__service.user_planes):
                                placed_planes+=1
                            else:
                                print("Invalid placement")
                                time.sleep(1)

                            if placed_planes == 3:
                                confirm_pos=0
                                while True:
                                    self.clear()
                                    for i in range(0,len(display_board)):
                                        print(display_board[i])
                                        
                                    print("Do you want to start the game?")
                                    if confirm_pos == 0:
                                        print(">YES   |    no")
                                    else:
                                        print(" yes   |   >NO")
                                
                                    key =kb.read_event()
                                    if key.event_type == "down":
                                        key = key.name
                                        match key:
                                            case "up":
                                                confirm_pos +=1
                                                if confirm_pos == 2:
                                                    confirm_pos = 0
                                            case "down":
                                                confirm_pos -=1
                                                if confirm_pos == -1:
                                                    confirm_pos = 1

                                            case "left":
                                                confirm_pos -=1
                                                if confirm_pos == -1:
                                                    confirm_pos = 1
                                            case "right":
                                                confirm_pos +=1
                                                if confirm_pos == 2:
                                                    confirm_pos = 0
                                            case "enter":
                                                if confirm_pos == 0:
                                                    self.__service.ai_add_plane()
                                                    self.__ingame()
                                                    self.__service.reset()
                                                    return
                                                else:
                                                    cursor_posx = 0
                                                    cursor_posy = 0
                                                    orientation = 0
                                                    placed_planes = 0
                                                    self.__service.reset()
                                                    break
                    
            

                


    def __load_game(self):
        cursor_poz =0
        while True:
            self.clear()
            print("======Load Game======")
            if self.__continue == False:
                print("No saved games")
                print("Do you want to start a new game?")
                if cursor_poz == 0:
                    print(">YES   |    no")
                else:
                    print(" yes   |   >NO")
               
                key =kb.read_event()
                if key.event_type == "down":
                    key = key.name
                    match key:
                        case "up":
                            cursor_poz +=1
                            if cursor_poz == 2:
                                cursor_poz = 0
                        case "down":
                            cursor_poz -=1
                            if cursor_poz == -1:
                                cursor_poz = 1

                        case "left":
                            cursor_poz -=1
                            if cursor_poz == -1:
                                cursor_poz = 1
                        case "right":
                            cursor_poz +=1
                            if cursor_poz == 2:
                                cursor_poz = 0
                        case "enter":
                            if cursor_poz == 0:
                                self.__new_game()
                            else:
                                break
            else:
                self.__service.load_game()

    def __main_menu(self):
        cursor =">"
        cursor_pos = 0
        empty = " "
        menu=["New game","Load game","Settings","Exit"]
        while True:
            self.clear()
            print("======Main Menu======")
            for i in range(len(menu)):
                if i == cursor_pos:
                    print(cursor,menu[i])
                else:
                    print(empty,menu[i])

            key = kb.read_event()
            if key.event_type == "down":
                key = key.name
                match key:
                    case "up":
                        cursor_pos-=1
                        if cursor_pos == -1:
                            cursor_pos = len(menu)-1
                    case "down":
                        cursor_pos+=1
                        if cursor_pos == len(menu):
                            cursor_pos = 0
                    case "enter":
                        match cursor_pos:
                            case 0:
                                self.__new_game()
                            case 1:
                                self.__load_game()
                            case 2:
                                self.__settings_menu()
                            case 3:
                                break

                        


    def run(self):
        self.__main_menu()

    
            



            
            
            


        