
from abc import ABC, abstractmethod


class Abstract(ABC):


    """
    :Var wert The value who needs to be converted into the new currency
    :var output the output of the API request
    :var symbols the goal currency
    :var base the start currency
    """
    def __init__(self):
        self.wert = None
        self.output = None
        self.symbols = None
        self.base = None


    """
    
    Calculates the result Data
    
    
    :param base the base currency for example "EUR"
    :param ziel the goal currency for example "USD,CAD"
    :param wert the how much money of the base currency you have
    
    :returns a String with all the information
    """
    @abstractmethod
    def requestData(self, base, ziel, wert):
        pass
