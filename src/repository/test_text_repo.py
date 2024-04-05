import sys
from pathlib import Path
path = Path().parent.absolute()
sys.path.insert(0, str(path))

from src.repository.Text_repo import get_text_repo
from unittest import TestCase
from io import StringIO
from unittest.mock import patch
from src.repository._Repo_except import LoadingError, FileNotFound

class TestTextRepo(TestCase):
    def setUp(self):
        self.repo = get_text_repo('test.txt')
        self.repo.empty()
        self.repo._save_to_file()

    def test_save(self):
        self.repo.add(1)
        self.repo.add(2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.repo)
            self.assertEqual(fake_out.getvalue(), "1\n2\n")
        self.repo._save_to_file()
        fin= open('test.txt', 'r')
        self.assertEqual(fin.read(), "[1, 2]")

    def test_load(self):
        self.repo._load_from_file()
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.repo)
            self.assertEqual(fake_out.getvalue(), "\n")

        self.repo.add(1)
        self.repo.add(2)
        self.repo._save_to_file()
        try:
            self.repo._load_from_file()
        except LoadingError as e:
            self.assertEqual(e._inspect_(), "The function _load_from_file exited with unpredictable return.\n")

            
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.repo)
            self.assertEqual(fake_out.getvalue(), "1\n2\n")
    
    def test_new_repo(self):
        try:
            repo=get_text_repo('')
            repo._load_from_file()
        except FileNotFound as e:
            self.assertEqual(e._inspect_(), "The function _load_from_file exited with unpredictable return.\n")

