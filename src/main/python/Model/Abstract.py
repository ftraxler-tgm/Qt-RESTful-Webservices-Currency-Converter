from abc import ABC, abstractmethod


class Abstract(ABC):
    """
    :ivar wert: The value who needs to be converted into the new currency
    :ivar output: the output of the API request
    :ivar symbols: the goal currency
    :ivar base: the start currency
    """
    def __init__(self):
        self.wert = None
        self.output = None
        self.symbols = None
        self.base = None

    @abstractmethod
    def requestData(self, base, ziel, wert):
        """
       Calculates the result Data


       :param base: The base currency for example "EUR"
       :param ziel: The goal currency for example "USD,CAD"
       :param wert: The how much money of the base currency you have

       :returns: A String with all the information
       """
        pass
