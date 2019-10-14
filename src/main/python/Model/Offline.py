from Model import Abstract
import json


class Offline(Abstract.Abstract):
    """
    The Oflline Class for the Offline-Usage

    :ivar file: The file where the data is saved for the offline-usage
    """

    def __init__(self):
        super().__init__()
        self.file = None

    def requestData(self, base, ziel, wert):
        """
        Sends a request to the API with a Json in return and  Calculates the new value for the new currency
        :param wert: The value who needs to be converted into the new currency
        :param ziel: The goal currency
        :param base: The start currency
        :returns: A String with all the information
       """

        self.wert = wert
        self.base = base
        self.symbols = str(ziel).split(',')
        with open('../api.json') as json_data:
            file = json.load(json_data)

        self.file = file

        print("Base: " + base + " Ziel: " + ziel)
        result = "<b>" + str(self.wert) + "</b> " + self.base + " entsprechen <br>"
        result += "<ul>"

        if base != "EUR":
            umrechnung = file['rates'][base]
            print("Wert in " + base + "  " + str(wert))
            print("Kurs für die Umrechung in EUR " + str(umrechnung))
            wert = float(wert / umrechnung)
            print("Wert in EUR " + str(wert))

        for x in self.symbols:
            if x == "EUR":
                result += "<li><b>" + str(wert) + "</b> EUR (Kurs: " + str(umrechnung) + ")</li>"
            else:
                kurs = self.file['rates'][x]
                result += "<li><b>" + str(kurs * self.wert) + "</b> " + x + " (Kurs: " + str(kurs) + ")</li>"

        result += "</ul><br>"
        result += "Stand: " + self.file['date']
        return result
