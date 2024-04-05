
import sys
from pathlib import Path
path = Path().parent.absolute()
sys.path.insert(0, str(path))


from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from src.services.Game_services import Game_services
from src.domain.Board import Board




class TestGame_serv(TestCase):
    def setUp(self):
        self.serv = Game_services(Board(),Board(),Board(),Board(),None)

    def test_init(self):
        self.assertEqual(str(self.serv.user_board), str(Board()))
        self.assertEqual(str(self.serv.computer_board), str(Board()))
        self.assertEqual(str(self.serv.user_strikes), str(Board()))
        self.assertEqual(str(self.serv.computer_strikes), str(Board()))
        self.assertEqual(self.serv.user_planes, [])
        self.assertEqual(self.serv.computer_planes, [])

    def test_add_plane(self):
        self.serv.add_plane(0,0,0,self.serv.user_board,self.serv.user_planes)
        self.assertEqual(self.serv.user_planes[0], [2,0])
        self.serv.add_plane(0,0,0,self.serv.computer_board,self.serv.computer_planes)
        self.assertEqual(self.serv.computer_planes[0], [2,0])

    def test_strike(self):
        self.serv.strike(0,0,self.serv.computer_board,self.serv.user_strikes)
        self.assertEqual(self.serv.user_strikes.get_simbol(0,0), '-')
        self.serv.strike(0,0,self.serv.user_board,self.serv.computer_strikes)
        self.assertEqual(self.serv.computer_strikes.get_simbol(0,0), '-')

    

        