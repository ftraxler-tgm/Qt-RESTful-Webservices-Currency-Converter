# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/waehrungGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(816, 338)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitB = QtWidgets.QPushButton(self.centralwidget)
        self.exitB.setGeometry(QtCore.QRect(20, 260, 361, 28))
        self.exitB.setObjectName("exitB")
        self.resetB = QtWidgets.QPushButton(self.centralwidget)
        self.resetB.setGeometry(QtCore.QRect(410, 260, 391, 28))
        self.resetB.setObjectName("resetB")
        self.textBrowserBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserBox.setGeometry(QtCore.QRect(20, 50, 781, 192))
        self.textBrowserBox.setObjectName("textBrowserBox")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(20, 298, 55, 16))
        self.status.setObjectName("status")
        self.liveCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.liveCheckbox.setGeometry(QtCore.QRect(703, 14, 91, 31))
        self.liveCheckbox.setObjectName("liveCheckbox")
        self.umrechnenB = QtWidgets.QPushButton(self.centralwidget)
        self.umrechnenB.setGeometry(QtCore.QRect(594, 15, 93, 28))
        self.umrechnenB.setObjectName("umrechnenB")
        self.waehrungText = QtWidgets.QLabel(self.centralwidget)
        self.waehrungText.setGeometry(QtCore.QRect(186, 20, 61, 16))
        self.waehrungText.setObjectName("waehrungText")
        self.zielwaehrung = QtWidgets.QLineEdit(self.centralwidget)
        self.zielwaehrung.setGeometry(QtCore.QRect(471, 18, 113, 22))
        self.zielwaehrung.setObjectName("zielwaehrung")
        self.zielwaehrungText = QtWidgets.QLabel(self.centralwidget)
        self.zielwaehrungText.setGeometry(QtCore.QRect(370, 20, 101, 16))
        self.zielwaehrungText.setObjectName("zielwaehrungText")
        self.waehrungInput = QtWidgets.QLineEdit(self.centralwidget)
        self.waehrungInput.setGeometry(QtCore.QRect(250, 18, 113, 22))
        self.waehrungInput.setObjectName("waehrungInput")
        self.betragText = QtWidgets.QLabel(self.centralwidget)
        self.betragText.setGeometry(QtCore.QRect(20, 20, 55, 16))
        self.betragText.setObjectName("betragText")
        self.betragSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.betragSpinBox.setGeometry(QtCore.QRect(77, 18, 101, 22))
        self.betragSpinBox.setObjectName("betragSpinBox")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Currency Converter"))
        self.exitB.setText(_translate("mainWindow", "Exit"))
        self.resetB.setText(_translate("mainWindow", "Zurücksetzen"))
        self.status.setText(_translate("mainWindow", "Status:"))
        self.liveCheckbox.setText(_translate("mainWindow", "Live-Daten"))
        self.umrechnenB.setText(_translate("mainWindow", "Umrechnen"))
        self.waehrungText.setText(_translate("mainWindow", "Währung::"))
        self.zielwaehrungText.setText(_translate("mainWindow", "Zielwährungen:"))
        self.betragText.setText(_translate("mainWindow", "Betrag:"))
