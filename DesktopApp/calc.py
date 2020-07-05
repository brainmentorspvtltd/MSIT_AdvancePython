from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(739, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(280, 10, 181, 51))
        self.headingLabel.setStyleSheet("color: rgb(252, 1, 7);\n"
                                        "font: 24pt \"Baghdad\";")
        self.headingLabel.setObjectName("headingLabel")
        self.firstNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNumberLabel.setGeometry(QtCore.QRect(130, 130, 181, 51))
        self.firstNumberLabel.setStyleSheet("color: rgb(252, 1, 7);\n"
                                            "font: 20pt \"Baghdad\";")
        self.firstNumberLabel.setObjectName("firstNumberLabel")
        self.secondNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondNumberLabel.setGeometry(QtCore.QRect(130, 220, 211, 51))
        self.secondNumberLabel.setStyleSheet("color: rgb(252, 1, 7);\n"
                                             "font: 20pt \"Baghdad\";")
        self.secondNumberLabel.setObjectName("secondNumberLabel")
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(130, 310, 211, 51))
        self.resultLabel.setStyleSheet("color: rgb(252, 1, 7);\n"
                                       "font: 20pt \"Baghdad\";")
        self.resultLabel.setObjectName("resultLabel")
        self.firstNumberTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNumberTextBox.setGeometry(QtCore.QRect(410, 130, 191, 41))
        self.firstNumberTextBox.setStyleSheet("font: 24pt \"Zapf Dingbats\";")
        self.firstNumberTextBox.setText("")
        self.firstNumberTextBox.setObjectName("firstNumberTextBox")
        self.secondNumberTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.secondNumberTextBox.setGeometry(QtCore.QRect(410, 220, 191, 41))
        self.secondNumberTextBox.setStyleSheet("font: 24pt \"Zapf Dingbats\";")
        self.secondNumberTextBox.setText("")
        self.secondNumberTextBox.setObjectName("secondNumberTextBox")
        self.resultTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.resultTextBox.setGeometry(QtCore.QRect(410, 310, 191, 41))
        self.resultTextBox.setStyleSheet("font: 24pt \"Zapf Dingbats\";")
        self.resultTextBox.setText("")
        self.resultTextBox.setObjectName("resultTextBox")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(100, 410, 113, 101))
        self.addButton.setStyleSheet("background-color: rgb(252, 1, 7);\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "font: 50pt \"Songti TC\";")
        self.addButton.setObjectName("addButton")
        self.subtractButton = QtWidgets.QPushButton(self.centralwidget)
        self.subtractButton.setGeometry(QtCore.QRect(240, 410, 113, 101))
        self.subtractButton.setStyleSheet("background-color: rgb(252, 1, 7);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 50pt \"Songti TC\";")
        self.subtractButton.setObjectName("subtractButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget)
        self.multiplyButton.setGeometry(QtCore.QRect(380, 410, 113, 101))
        self.multiplyButton.setStyleSheet("background-color: rgb(252, 1, 7);\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "font: 50pt \"Songti TC\";")
        self.multiplyButton.setObjectName("multiplyButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget)
        self.divideButton.setGeometry(QtCore.QRect(520, 410, 113, 101))
        self.divideButton.setStyleSheet("background-color: rgb(252, 1, 7);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 50pt \"Songti TC\";")
        self.divideButton.setObjectName("divideButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.headingLabel.setText(_translate("MainWindow", "Basic Calculator"))
        self.firstNumberLabel.setText(
            _translate("MainWindow", "Enter First Number"))
        self.secondNumberLabel.setText(
            _translate("MainWindow", "Enter Second Number"))
        self.resultLabel.setText(_translate("MainWindow", "Result"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.subtractButton.setText(_translate("MainWindow", "-"))
        self.multiplyButton.setText(_translate("MainWindow", "*"))
        self.divideButton.setText(_translate("MainWindow", "/"))

        self.addButton.clicked.connect(self.add)
        self.subtractButton.clicked.connect(self.sub)
        self.multiplyButton.clicked.connect(self.mul)
        self.divideButton.clicked.connect(self.div)

    def getNumbers(self):
        f_num = int(self.firstNumberTextBox.text())
        s_num = int(self.secondNumberTextBox.text())
        return f_num, s_num

    def add(self):
        x, y = self.getNumbers()
        result = str(x+y)
        self.resultTextBox.setText(result)
        # print("Add called...")

    def sub(self):
        x, y = self.getNumbers()
        result = str(x-y)
        self.resultTextBox.setText(result)
        # print("Sub called...")

    def mul(self):
        x, y = self.getNumbers()
        result = str(x*y)
        self.resultTextBox.setText(result)
        # print("Mul called...")

    def div(self):
        x, y = self.getNumbers()
        result = str(x/y)
        self.resultTextBox.setText(result)
        # print("Div called...")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
