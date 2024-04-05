import sys
from pathlib import Path

path=Path().parent.absolute()
sys.path.insert(0, str(path))

from src.repository._Repo_except import FileNotFound
from src.repository.Memory_repo import Repo

class Text_Repo(Repo):
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def _save_to_file(self):
        '''
            saves the data to the file
        '''
        fout = open(self._file_name, "wt")
        if len(self._data)==0:
            fout.close()
            return
        fout.write(self._data.__repr__())

        fout.close()

    def _load_from_file(self):
        '''
            loads the data from the file if posible
        '''
        self._data=[]
        try:
            fin = open(self._file_name, "rt")
        except:
            raise FileNotFound(self._file_name)
        
        command = fin.readline().strip()
        if command == "":
            fin.close()
            return

        self._data=eval(command)
        fin.close()


def get_text_repo(file_name):
    '''
        returns a loaded text repo
    '''
    text_rep = Text_Repo(file_name)
    try:
        text_rep._load_from_file()
    except:
        pass
    return text_rep