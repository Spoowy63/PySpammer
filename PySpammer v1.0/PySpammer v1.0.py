from PyQt5 import QtCore, QtWidgets, QtGui
import webbrowser
import pyautogui
from time import sleep
from random import choice
from io import BytesIO
import win32clipboard
from PIL import Image
import os
import pyperclip
import codecs
import requests

cc = codecs.decode("ZNQR OL tvguho.pbz/Fcbbjl63", encoding='rot13')

symbS = open('symbol.txt', 'r').read()

symbolText = bytes.fromhex(symbS).decode('utf-8')

github = codecs.decode("uggcf://tvguho.pbz/Fcbbjl63?gno=ercbfvgbevrf", encoding='rot13')
telegram = codecs.decode("uggcf://g.zr/fcbbjl63", encoding='rot13')

buttonStyleSheet = "QPushButton { color: rgb(255, 255, 255);" "background-color: rgba(0, 255, 255, 0);" "border: 1.5px solid white;" "border-radius: 8px;" "font: 75 14pt \"Arial\"}" "QPushButton:pressed { background-color: rgb(255, 255, 255);" "color: rgb(43, 47, 59)}" "QComboBox {background-color: rgba(0, 0, 0, 0);\n"
comboBoxStyleSheet = "QPushButton { color: rgb(255, 255, 255);" "background-color: rgba(0, 255, 255, 0);" "border: 1.5px solid white;" "border-radius: 8px;" "font: 75 14pt \"Arial\"}" "QPushButton:pressed { background-color: rgb(255, 255, 255);" "color: rgb(43, 47, 59)}" "QComboBox {background-color: rgba(0, 0, 0, 0);" "color: rgb(255, 255, 255);" "background-color: rgba(0, 255, 255, 0);" "border: 1.5px solid white;" "border-radius: 4px;" "padding: 1px 0px 1px 5px;" "font: 75 14pt \"Arial\";" "} QComboBox QAbstractItemView {border: 2px solid white; selection-background-color: rgba(0, 0, 0, 255); background-color: rgb(43, 47, 59); color: white; selection-background-color: rgb(255, 255, 255); selection-color: rgb(43, 47, 59);}"
lineEditStyleSheet = "background-color: rgba(0, 0, 0, 0);" "color: rgb(255, 255, 255);" "border: 1.5px solid white;" "border-radius: 8px;" "padding: 1px 0px 1px 5px;" "font: 75 14pt \"Arial\";"
labelStyleSheet = "background-color: rgba(0, 0, 0, 0);" "color: rgb(255, 255, 255);" "font: 75 18pt \"Arial\";"


def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 525)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 525))
        MainWindow.setMaximumSize(QtCore.QSize(500, 525))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        MainWindow.setStyleSheet("background-color: rgb(43, 47, 59);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 430, 120, 51))
        self.pushButton.setStyleSheet(buttonStyleSheet)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 430, 120, 51))
        self.pushButton_2.setStyleSheet(buttonStyleSheet)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 430, 120, 51))
        self.pushButton_3.setStyleSheet(buttonStyleSheet)
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 60, 280, 31))
        self.comboBox.setStyleSheet(comboBoxStyleSheet)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 340, 170, 31))
        self.lineEdit_3.setStyleSheet(lineEditStyleSheet)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 10, 190, 41))
        self.label.setStyleSheet(labelStyleSheet)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 350, 31))
        self.label_2.setStyleSheet(labelStyleSheet)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 290, 251, 31))
        self.label_3.setStyleSheet(labelStyleSheet)
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 230, 170, 31))
        self.lineEdit_4.setStyleSheet(lineEditStyleSheet)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setVisible(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 120, 330, 31))
        self.lineEdit_5.setStyleSheet(lineEditStyleSheet)
        self.lineEdit_5.setObjectName("lineEdit_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_2.clicked.connect(self.github_link)
        self.pushButton_3.clicked.connect(self.telegram_link)
        self.pushButton.clicked.connect(self.pressed)
        self.comboBox.currentTextChanged.connect(self.combobox_changed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySpammer v1.0"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "GITHUB"))
        self.pushButton_3.setText(_translate("MainWindow", "TELEGRAM"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Choose From Here..."))
        self.comboBox.setItemText(1, _translate("MainWindow", "Custom text spam"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Random sentences spam"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Symbol spam"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Random image spam (Folder)"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Random image spam (Links)"))
        self.label.setText(_translate("MainWindow", "Choose an option"))
        self.label_2.setText(_translate("MainWindow", "How many times should it spam"))
        self.label_3.setText(_translate("MainWindow", "Interval after each msg (sec)"))

    def combobox_changed(self, value):
        if value == "Custom text spam":
            self.lineEdit_5.setVisible(True)
        else:
            self.lineEdit_5.setVisible(False)

    def github_link(self):
        webbrowser.open(github)

    def telegram_link(self):
        webbrowser.open(telegram)

    def pressed(self):
        text = self.comboBox.currentText()

        sleep(3)

        textto = self.lineEdit_5.text()
        amount = int(self.lineEdit_4.text())
        time = self.lineEdit_3.text()

        for _ in range(amount):
            if text == "Random sentences spam":
                tex = open("text.txt", "r", encoding="utf8").read()
                tex = tex.splitlines()
                pyautogui.typewrite(choice(tex))
                pyautogui.press("enter")
                if time == "":
                    sleep(0.0)
                else:
                    timeoutSpam = float(time)
                    sleep(timeoutSpam)

            elif text == "Random image spam (Folder)":
                path0 = os.path.dirname(os.path.realpath(__file__))
                path = os.path.join(path0, "imgss")
                random_filename = choice([
                    x for x in os.listdir(path)
                    if os.path.isfile(os.path.join(path, x))
                ])
                image = Image.open(os.path.join(path, random_filename))

                output = BytesIO()
                image.convert("RGB").save(output, "BMP")
                data = output.getvalue()[14:]
                output.close()

                send_to_clipboard(win32clipboard.CF_DIB, data)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")
                pyautogui.press("enter")
                if time == "":
                    sleep(0.0)
                else:
                    timeoutSpam = float(time)
                    sleep(timeoutSpam)

            elif text == "Custom text spam":
                pyautogui.typewrite(textto)
                pyautogui.press("enter")
                if time == "":
                    sleep(0.0)
                else:
                    timeoutSpam = float(time)
                    sleep(timeoutSpam)

            elif text == "Random image spam (Links)":
                randomUrl = requests.head("https://source.unsplash.com/random/", allow_redirects=True)
                pyautogui.typewrite(randomUrl.url)
                pyautogui.press("enter")
                if time == "":
                    sleep(0.0)
                else:
                    timeoutSpam = float(time)
                    sleep(timeoutSpam)

            elif text == "Symbol spam":
                pyperclip.copy(symbolText)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press("enter")
                if time == "":
                    sleep(0.0)
                else:
                    timeoutSpam = float(time)
                    sleep(timeoutSpam)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
