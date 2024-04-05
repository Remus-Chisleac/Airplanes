

class Planes():
    '''
        class that stores all the posible planes
    '''
    def plane_nord(self):
        return 2,0,[[' ',' ','H',' ',' '],
                    ['B','B','B','B','B'],
                    [' ',' ','B',' ',' '],
                    [' ','B','B','B',' ']]
    
    def plane_south(self):
        return 2,3,[[' ','B','B','B',' '],
                    [' ',' ','B',' ',' '],
                    ['B','B','B','B','B'],
                    [' ',' ','H',' ',' ']]

    def plane_east(self):
        return 3,2,[[' ',' ','B',' '],
                    ['B',' ','B',' '],
                    ['B','B','B','H'],
                    ['B',' ','B',' '],
                    [' ',' ','B',' ']]

    def plane_west(self):
        return 0,2,[[' ','B',' ',' '],
                    [' ','B',' ','B'],
                    ['H','B','B','B'],
                    [' ','B',' ','B'],
                    [' ','B',' ',' ']]