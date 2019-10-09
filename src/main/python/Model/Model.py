import requests,json
class Rest:

    def __init__(self):
        self.base= None
        self.symbols = None
        self.wert = None
        self.output = None
        self.online = True


    def umrechnen(self,):
        result = str(self.wert) + " " + self.base + " entsprechen \n\n"
        # kurs = output['rates'][symbols]
        for x in self.symbols:
            kurs = self.output['rates'][x]
            result += "\t" + str(kurs * self.wert) + " " + x + " (Kurs: " + str(kurs) + ")\n"

        result += "\n\nStand: " + self.output['date']
        print(result)

        return result


    def requestData(self,base,ziel,wert):
        self.wert=wert
        self.base=base
        self.symbols=str(ziel).split(',')

        print(self.online)

        if(self.online):
            url = "https://api.exchangeratesapi.io/latest"
            output=""
            params = {"base": base,
                      "symbols": ziel,
                      }
            resp = requests.get(url, params=params)
            output = ""
            if resp.status_code != 200:
                output= resp.json()
                raise ValueError("Request failed")

            else:
                output = resp.json()
                self.output=output
                return (self.umrechnen())
        else:
            with open('../api.json') as json_data:
                file= json.load(json_data)







