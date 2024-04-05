
import sys
from pathlib import Path
path = Path().parent.absolute()
sys.path.insert(0, str(path))


from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from src.services.Game_services import Settings




class TestGame_Settings(TestCase):
    def setUp(self):
        self.sett= Settings()

    def test_init(self):
        self.assertEqual(self.sett.poz, [0,0,1,1])
    
    def test_tutorial(self):
        self.assertEqual(self.sett.tutorial, "On")
        self.sett.add_tutorial()
        self.assertEqual(self.sett.tutorial, "Off")
        self.sett.sub_tutorial()
        self.assertEqual(self.sett.tutorial, "On")
    
    def test_difficulty(self):
        self.assertEqual(self.sett.difficulty, "Easy")
        self.sett.add_difficulty()
        self.assertEqual(self.sett.difficulty, "Medium")
        self.sett.add_difficulty()
        self.assertEqual(self.sett.difficulty, "Hard")
        self.sett.sub_difficulty()
        self.assertEqual(self.sett.difficulty, "Medium")
        self.sett.sub_difficulty()
        self.assertEqual(self.sett.difficulty, "Easy")

    def test_downed_plane(self):
        self.assertEqual(self.sett.downed_plane, "Reveal_head")
        self.sett.add_downed_plane()
        self.assertEqual(self.sett.downed_plane, "Off")
        self.sett.add_downed_plane()
        self.assertEqual(self.sett.downed_plane, "Reveal_full")
        self.sett.sub_downed_plane()
        self.assertEqual(self.sett.downed_plane, "Off")
        self.sett.sub_downed_plane()
        self.assertEqual(self.sett.downed_plane, "Reveal_head")
    
    def test_second_wind(self):
        self.assertEqual(self.sett.second_wind, "Off")
        self.sett.add_second_wind()
        self.assertEqual(self.sett.second_wind, "On")
        self.sett.sub_second_wind()
        self.assertEqual(self.sett.second_wind, "Off")
        