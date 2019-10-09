
from abc import *
class Request(ABC):

    def __init__(self):
        self.base = None
        self.symbols = None
        self.wert = None
        self.output = None
        self.online = True

    @abstractmethod
    def requestData(self):
        pass