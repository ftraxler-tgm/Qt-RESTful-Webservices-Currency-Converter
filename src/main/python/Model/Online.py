import requests

from Model import Abstract


class Online(Abstract.Abstract):

    def __init__(self):
        super().__init__()


    def umrechnen(self):
        result = "<b>" + str(self.wert) + "</b> " + self.base + " entsprechen <br>"
        # kurs = output['rates'][symbols]
        result+="<ul>"
        for x in self.symbols:
            kurs = self.output['rates'][x]
            result += "<li><b>" + str(kurs * self.wert) + "</b> " + x + " (Kurs: " + str(kurs) + ")</li>"


        result+= "</ul><br>"
        result += "Stand: " + self.output['date']
        #print(result)

        return result

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
