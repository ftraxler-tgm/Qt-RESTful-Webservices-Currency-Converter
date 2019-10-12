import requests

from Model import Abstract


class Online(Abstract.Abstract):

    def __init__(self):
        super().__init__()


    """
    Calculates the new value for the new currency and creates a useful output
    
    :return A HTMl output as String
    """
    def umrechnen(self):
        result = "<b>" + str(self.wert) + "</b> " + self.base + " entsprechen <br>"
        # kurs = output['rates'][symbols]
        result += "<ul>"
        for x in self.symbols:
            kurs = self.output['rates'][x]
            result += "<li><b>" + str(kurs * self.wert) + "</b> " + x + " (Kurs: " + str(kurs) + ")</li>"

        result += "</ul><br>"
        result += "Stand: " + self.output['date']
        # print(result)

        return result


    """
    
    Sends a request to the API with a Json in return and forwards the data to umrechnen
    :Var wert The value who needs to be converted into the new currency
    :var ziel the goal currency
    :var base the start currency
    
    :return A String with all the information
    """
    def requestData(self, base, ziel, wert):
        self.wert = wert
        self.base = base
        self.symbols = str(ziel).split(',')

        url = "https://api.exchangeratesapi.io/latest"
        output = ""
        params = {"base": base,
                  "symbols": ziel,
                  }
        resp = requests.get(url, params=params)
        output = ""
        if resp.status_code != 200:
            output = resp.json()
            raise ValueError("Request failed")

        else:
            output = resp.json()
            self.output = output
            return self.umrechnen()
