import sys
from pathlib import Path

path=Path().parent.absolute()
sys.path.insert(0, str(path))

from src._exceptions._Except import _except

class FileNotFound(_except):
    def __init__(self, filename,message=''):
        super().__init__()
        self.filename = filename
        self.message=message

    def __str__(self):
        output=self._inspect_()+"File not found: "+self.filename
        if self.message!="":
            output+="\n"+self.message
        return output


class LoadingError(_except):
    def __init__(self, filename,message=''):
        super().__init__()
        self.filename = filename
        self.message=message


    def __str__(self):
        output=self._inspect_()+"Error loading file: "+self.filename
        if self.message!="":
            output+="\n"+self.message
        return output