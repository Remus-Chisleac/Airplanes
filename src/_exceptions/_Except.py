import inspect
class _except(Exception):
    def __init__(self):
        i=1
        self.function_name=inspect.stack()[i][3]
        while self.function_name=="__init__":
            i+=1
            self.function_name=inspect.stack()[i][3]

    def __str__(self) -> str:
        return "The function {} exited with unpredictable return.\n".format(self.function_name)

    def _inspect_(self) -> str:
        return "The function {} exited with unpredictable return.\n".format(self.function_name)