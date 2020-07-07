from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 614)
        MainWindow.setStyleSheet("background-color: rgb(68, 69, 71);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 441, 71))
        self.lineEdit.setStyleSheet("font: 50pt \"Futura\";\n"
                                    "color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.resetBtn = QtWidgets.QPushButton(self.centralwidget)
        self.resetBtn.setGeometry(QtCore.QRect(0, 70, 113, 101))
        self.resetBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                    "background-color: rgb(81, 81, 84);\n"
                                    "color: rgb(255, 255, 255);")
        self.resetBtn.setObjectName("resetBtn")
        self.toggleSignBtn = QtWidgets.QPushButton(self.centralwidget)
        self.toggleSignBtn.setGeometry(QtCore.QRect(110, 70, 113, 101))
        self.toggleSignBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                         "background-color: rgb(81, 81, 84);\n"
                                         "color: rgb(255, 255, 255);")
        self.toggleSignBtn.setObjectName("toggleSignBtn")
        self.percentBtn = QtWidgets.QPushButton(self.centralwidget)
        self.percentBtn.setGeometry(QtCore.QRect(220, 70, 113, 101))
        self.percentBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                      "background-color: rgb(81, 81, 84);\n"
                                      "color: rgb(255, 255, 255);")
        self.percentBtn.setObjectName("percentBtn")
        self.divideBtn = QtWidgets.QPushButton(self.centralwidget)
        self.divideBtn.setGeometry(QtCore.QRect(330, 70, 113, 101))
        self.divideBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                     "background-color: rgb(240, 141, 49);")
        self.divideBtn.setObjectName("divideBtn")
        self.nineBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nineBtn.setGeometry(QtCore.QRect(220, 170, 113, 101))
        self.nineBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(108, 108, 111);")
        self.nineBtn.setObjectName("nineBtn")
        self.multiplyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyBtn.setGeometry(QtCore.QRect(330, 170, 113, 101))
        self.multiplyBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                       "background-color: rgb(240, 141, 49);")
        self.multiplyBtn.setObjectName("multiplyBtn")
        self.eightBtn = QtWidgets.QPushButton(self.centralwidget)
        self.eightBtn.setGeometry(QtCore.QRect(110, 170, 113, 101))
        self.eightBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(108, 108, 111);")
        self.eightBtn.setObjectName("eightBtn")
        self.sevenBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sevenBtn.setGeometry(QtCore.QRect(0, 170, 113, 101))
        self.sevenBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(108, 108, 111);")
        self.sevenBtn.setObjectName("sevenBtn")
        self.sixBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sixBtn.setGeometry(QtCore.QRect(220, 270, 113, 101))
        self.sixBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(108, 108, 111);")
        self.sixBtn.setObjectName("sixBtn")
        self.subtractBtn = QtWidgets.QPushButton(self.centralwidget)
        self.subtractBtn.setGeometry(QtCore.QRect(330, 270, 113, 101))
        self.subtractBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                       "background-color: rgb(240, 141, 49);")
        self.subtractBtn.setObjectName("subtractBtn")
        self.fiveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fiveBtn.setGeometry(QtCore.QRect(110, 270, 113, 101))
        self.fiveBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(108, 108, 111);")
        self.fiveBtn.setObjectName("fiveBtn")
        self.fourBtn = QtWidgets.QPushButton(self.centralwidget)
        self.fourBtn.setGeometry(QtCore.QRect(0, 270, 113, 101))
        self.fourBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(108, 108, 111);")
        self.fourBtn.setObjectName("fourBtn")
        self.threeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.threeBtn.setGeometry(QtCore.QRect(220, 370, 113, 101))
        self.threeBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(108, 108, 111);")
        self.threeBtn.setObjectName("threeBtn")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(330, 370, 113, 101))
        self.addBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                  "background-color: rgb(240, 141, 49);")
        self.addBtn.setObjectName("addBtn")
        self.twoBtn = QtWidgets.QPushButton(self.centralwidget)
        self.twoBtn.setGeometry(QtCore.QRect(110, 370, 113, 101))
        self.twoBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(108, 108, 111);")
        self.twoBtn.setObjectName("twoBtn")
        self.oneBtn = QtWidgets.QPushButton(self.centralwidget)
        self.oneBtn.setGeometry(QtCore.QRect(0, 370, 113, 101))
        self.oneBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(108, 108, 111);")
        self.oneBtn.setObjectName("oneBtn")
        self.decimalPointBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decimalPointBtn.setGeometry(QtCore.QRect(222, 470, 111, 101))
        self.decimalPointBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color: rgb(108, 108, 111);")
        self.decimalPointBtn.setObjectName("decimalPointBtn")
        self.equalsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.equalsBtn.setGeometry(QtCore.QRect(330, 470, 113, 101))
        self.equalsBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                     "background-color: rgb(240, 141, 49);")
        self.equalsBtn.setObjectName("equalsBtn")
        self.zeroBtn = QtWidgets.QPushButton(self.centralwidget)
        self.zeroBtn.setGeometry(QtCore.QRect(0, 470, 221, 101))
        self.zeroBtn.setStyleSheet("font: 40pt \"Gill Sans\";\n"
                                   "color: rgb(255, 255, 255);\n"
                                   "background-color: rgb(108, 108, 111);")
        self.zeroBtn.setObjectName("zeroBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.resetBtn.setText(_translate("MainWindow", "AC"))
        self.toggleSignBtn.setText(_translate("MainWindow", "+/-"))
        self.percentBtn.setText(_translate("MainWindow", "%"))
        self.divideBtn.setText(_translate("MainWindow", "/"))
        self.nineBtn.setText(_translate("MainWindow", "9"))
        self.multiplyBtn.setText(_translate("MainWindow", "*"))
        self.eightBtn.setText(_translate("MainWindow", "8"))
        self.sevenBtn.setText(_translate("MainWindow", "7"))
        self.sixBtn.setText(_translate("MainWindow", "6"))
        self.subtractBtn.setText(_translate("MainWindow", "-"))
        self.fiveBtn.setText(_translate("MainWindow", "5"))
        self.fourBtn.setText(_translate("MainWindow", "4"))
        self.threeBtn.setText(_translate("MainWindow", "3"))
        self.addBtn.setText(_translate("MainWindow", "+"))
        self.twoBtn.setText(_translate("MainWindow", "2"))
        self.oneBtn.setText(_translate("MainWindow", "1"))
        self.decimalPointBtn.setText(_translate("MainWindow", "."))
        self.equalsBtn.setText(_translate("MainWindow", "="))
        self.zeroBtn.setText(_translate("MainWindow", "0"))
        self.lineEdit.setReadOnly(True)
        self.btns = [self.zeroBtn, self.decimalPointBtn, self.oneBtn, self.twoBtn, self.threeBtn, self.fourBtn, self.fiveBtn, self.sixBtn, self.sevenBtn,
                     self.eightBtn, self.nineBtn, self.addBtn, self.subtractBtn, self.multiplyBtn, self.divideBtn, self.percentBtn]
        self.operators = [self.addBtn, self.subtractBtn,
                          self.multiplyBtn, self.divideBtn, self.percentBtn]

        for btn in self.btns:
            btn.clicked.connect(self.appendValues)
        self.resetBtn.clicked.connect(self.resetText)
        self.toggleSignBtn.clicked.connect(self.toggleSign)
        self.equalsBtn.clicked.connect(self.calculate)
        self.isDecimalUsed = False
        self.isResultVisible = False

    def resetText(self):
        self.lineEdit.setText("")
        self.isDecimalUsed = False

    def toggleSign(self):
        text = self.lineEdit.text()
        if text.startswith("-"):
            text = text[1:]
        else:
            text = "-" + text
        self.lineEdit.setText(text)

    def appendValues(self):
        btn = self.sender()
        text = self.lineEdit.text()

        if len(text) == 14:
            pass
        elif btn in self.operators:
            self.isResultVisible = False
            self.isDecimalUsed = False
            if len(text) == 1:
                pass
            elif len(text) > 0:
                if ord(text[-1]) >= 48 and ord(text[-1]) <= 57:
                    text += btn.text()
                else:
                    text = text[:-1] + btn.text()
            elif btn == self.subtractBtn:
                text = btn.text()
        elif self.isResultVisible:
            self.lineEdit.setText("")
            text = btn.text()
            self.isResultVisible = False
        elif btn == self.decimalPointBtn:
            if not self.isDecimalUsed:
                text += btn.text()
                self.isDecimalUsed = True
        else:
            text += btn.text()

        self.lineEdit.setText(text)
        # print("Some btn clicked...")

    def calculate(self):
        text = self.lineEdit.text()
        if len(text) > 0:
            if ord(text[-1]) >= 48 and ord(text[-1]) <= 57:
                result = str(eval(text))
                if result != text:
                    self.lineEdit.setText(result[:14])
                    self.isResultVisible = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
