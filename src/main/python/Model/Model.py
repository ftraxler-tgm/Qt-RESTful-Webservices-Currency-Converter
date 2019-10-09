import requests
class Rest:

    def __init__(self):
        self.waehrung1 = None
        self.waehrung2 = None


    def umrechnen(self,symbols,output,base,wert):
        result = str(wert) + " " + base + " entsprechen \n\n"
        # kurs = output['rates'][symbols]
        for x in symbols:
            kurs = output['rates'][x]
            result += "\t" + str(kurs * wert) + " " + x + " (Kurs: " + str(kurs) + ")\n"

        result += "\n\nStand: " + output['date']
        print(result)

        return result


    def Online(self,base,ziel,wert):

        symbols=str(ziel).split(',')

        print(symbols)




        url = "https://api.exchangeratesapi.io/latest"
        output=""
        params = {"base": base,
                  "symbols": ziel,
                  }


        print(params)
        resp = requests.get(url, params=params)
        output = ""

        if resp.status_code != 200:
            output= resp.json()
            raise ValueError("Request failed")

        else:
            output = resp.json()
            print(output)
            self.umrechnen(symbols,output,base,wert)









