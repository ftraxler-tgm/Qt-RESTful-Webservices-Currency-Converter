from abc import ABC, abstractmethod


class Abstract(ABC):

    def __init__(self):
        self.wert = None
        self.output = None
        self.symbols = None
        self.base = None

    @abstractmethod
    def requestData(self, base, ziel, wert):
        pass
