
import sys
from pathlib import Path

path=Path().parent.absolute()
sys.path.insert(0, str(path))





class Repo(object):

    def __init__(self):
        self._data = []

    def add(self, obj):
        '''
        Adds an object to the repository
        :param obj: the object to be added
        :return: -
        '''
        self._data.append(obj)

    def insert(self, obj, index):
        self._data.insert(index, obj)

    def remove(self, obj):
        self._data.remove(obj)

    def update(self, old_obj, new_obj):
        self._data[self._data.index(old_obj)] = new_obj

    def empty(self):
        self._data = []

    def get_all(self):
        return self._data[:]
    
    def get_start_end(self,start:int,end:int):
        return self._data[start:end+1]

    def __len__(self):
        return len(self._data)

    def __str__(self):
        sol=""
        for obj in self._data:
            sol+=str(obj)
            sol+="\n"
        sol=sol[:-1]
        return sol
    
    def __iter__(self):
        return iter(self._data)

def get_memory_repo():
    '''
        return a memory repo
    '''
    return Repo()


