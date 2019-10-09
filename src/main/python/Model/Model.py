import requests
class Rest:

    def __init__(self):
        self.waehrung1 = None
        self.waehrung2 = None

    def umrechnen(self,base,symbols,wert):


        url = "https://api.exchangeratesapi.io/latest"
        output=""
        params = {"base": base,
                  "symbols": symbols,
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
            kurs = output['rates'][symbols]


        result= str(wert)+" " + base+ " entsprechen \n\n"
        result+=str(kurs*wert)+" "+symbols+" (Kurs: "+str(kurs)+")\n\n"

        result+="Stand: "+output['date']
        print(result)

        return result








