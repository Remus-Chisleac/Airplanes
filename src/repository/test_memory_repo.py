import sys
from pathlib import Path
path = Path().parent.absolute()
sys.path.insert(0, str(path))

from src.repository.Memory_repo import get_memory_repo
from unittest import TestCase
from io import StringIO
from unittest.mock import patch



class TestMemoryRepo(TestCase):
    def setUp(self):
        self.repo = get_memory_repo()
    
    def test_add(self):
        self.repo.add(1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.repo)
            self.assertEqual(fake_out.getvalue(), "1\n")

    def test_remove(self):
        self.repo.add(1)
        self.repo.remove(1)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.repo)
            self.assertEqual(fake_out.getvalue(), "\n")

    def test_get_all(self):
        self.repo.add(1)
        self.repo.add(2)
        self.repo.add(3)
        self.assertEqual(self.repo.get_all(), [1,2,3])

    def test_empty(self):
        self.repo.empty()
        self.assertEqual(len(self.repo), 0)

    def test_get_start_end(self):
        self.repo.add(1)
        self.repo.add(2)
        self.repo.add(3)
        self.assertEqual(self.repo.get_start_end(0,1), [1,2])
    
    def test_update(self):
        self.repo.add(1)
        self.repo.add(2)
        self.repo.add(3)
        self.repo.update(1,2)
        self.assertEqual(self.repo.get_all(), [2,2,3])
    
    def test_iter(self):
        self.repo.add(1)
        self.repo.add(2)
        self.repo.add(3)
        self.assertEqual(list(self.repo), [1,2,3])

    