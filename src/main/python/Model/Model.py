import requests
class Rest:

    def __init__(self):
        self.waehrung1 = None
        self.waehrung2 = None

    def umrechnen(self,base,symbols):


        url = "https://api.exchangeratesapi.io/latest"
        output=""
        params = {"base": "USD",
                  "symbols": "EUR"
                  }


        resp = requests.get(url, params=params)
        output = ""
        if resp.status_code != 200:
            output= resp.json()

        else:
            output = resp.json()
            kurs = output['rates'][]
            print(output['rates']['EUR'])








