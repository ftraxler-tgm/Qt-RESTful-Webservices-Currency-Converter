from View import WaehrungGui
from Model import Model
from PyQt5.QtWidgets import *
import sys


class Controller(QMainWindow):
    '''
    :var
    '''
    def __init__(self , parent = None):
        super().__init__(parent)
        self.model = Model.Rest()
        self.main_form = WaehrungGui.Ui_mainWindow()
        self.main_form.setupUi(self)
        self.main_form.exitB.clicked.connect(self.exitButton)
        self.main_form.resetB.clicked.connect(self.zuruecksetzen)
        self.main_form.umrechnenB.clicked.connect(self.umrechnen)


    def exitButton(self):

        sys.exit()

    def zuruecksetzen(self):
        self.main_form.betragSpinBox.setValue(0)
        self.main_form.betragSpinBox.cleanText()
        self.main_form.waehrungInput.clear()
        self.main_form.textBrowserBox.clear()
        self.main_form.zielwaehrung.clear()
        self.main_form.liveCheckbox.setChecked(False)
        print("All fields have been cleared")


    def umrechnen(self):
        try:
            request=self.model.umrechnen(self.main_form.waehrungInput.text().__str__(),self.main_form.zielwaehrung.text().__str__(),100.0)
            self.main_form.textBrowserBox.setText(request)
            self.main_form.status.setText(self.main_form.status.text().__str__()+" Ok")
        except ValueError as e:
            self.main_form.status.setText(self.main_form.status.text().__str__()+e.__str__())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())
