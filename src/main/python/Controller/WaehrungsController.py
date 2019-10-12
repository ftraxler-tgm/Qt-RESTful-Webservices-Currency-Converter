from View import WaehrungGui
from Model import Online
from Model import Offline
from PyQt5.QtWidgets import *
import sys, requests, json


class Controller(QMainWindow):
    '''

    MVC pattern: Creates a controller according to the mvc pattern.
    :var main_form: Qt Form
    :var model: The Calculation and Rest Request

    '''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = Online.Online()
        self.main_form = WaehrungGui.Ui_mainWindow()
        self.main_form.setupUi(self)
        self.main_form.exitB.clicked.connect(self.exitButton)
        self.main_form.resetB.clicked.connect(self.zuruecksetzen)
        self.main_form.umrechnenB.clicked.connect(self.umrechnen)
        self.main_form.liveCheckbox.stateChanged.connect(self.liveData)

        resp = requests.get("https://api.exchangeratesapi.io/latest")
        file = open("../api.json", "w")
        file.write(resp.text)
    """
    Changes the data source when you change from Live to Offline or the other way around
    """
    def liveData(self):
        if self.main_form.liveCheckbox.isChecked():
            print("Switched to Live Data")
            self.model = Online.Online()
            self.umrechnen()
        else:
            print("Switched to Offline Data")
            self.model = Offline.Offline()
            self.umrechnen()

    """
    Ends the programm
    """
    def exitButton(self):
        sys.exit()

    """
    Resets all textfields and does a request from the exchange api and saves it into a file
    """
    def zuruecksetzen(self):
        self.main_form.betragSpinBox.setValue(0)
        self.main_form.betragSpinBox.cleanText()
        self.main_form.waehrungInput.clear()
        self.main_form.textBrowserBox.clear()
        self.main_form.zielwaehrung.clear()
        self.main_form.status.setText("Status:")
        print("All fields have been cleared")

        resp = requests.get("https://api.exchangeratesapi.io/latest")
        file = open("../api.json", "w")
        file.write(resp.text)


    """
    Sends the request to the model und prints out the response
    """
    def umrechnen(self):
        try:
            request = self.model.requestData(self.main_form.waehrungInput.text().__str__(),
                                             self.main_form.zielwaehrung.text().__str__(), float(self.main_form.betragSpinBox.value().__str__()))
            self.main_form.status.setText("Status: Ok")
            self.main_form.textBrowserBox.setHtml(request)

        except ValueError as e:
            self.main_form.status.setText("Status: " + e.__str__())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
