import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QRadioButton, QButtonGroup)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.radio1 = QRadioButton("Deutsch", self)
        self.radio2 = QRadioButton("English", self)
        self.radio3 = QRadioButton("Dansk", self)
        self.radio4 = QRadioButton("Untertitel", self)
        self.radio5 = QRadioButton("Original", self)
        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)
        self.InitUI()

    def InitUI(self):
        self.radio1.setGeometry(0,0,500,50)
        self.radio2.setGeometry(0,50,500,50)
        self.radio3.setGeometry(0,100,500,50)
        self.radio4.setGeometry(0,200,500,50)
        self.radio5.setGeometry(0,250,500,50)

        self.setStyleSheet("QRadioButton{" \
                           "font-size: 35px;" \
                           "font-Family: Calibri;"
                           "}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()