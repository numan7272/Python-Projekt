import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QVBoxLayout, QGridLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)

        self.InitUI()

    def InitUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("Nummer 1", self)
        label2 = QLabel("Nummer 2", self)
        label3 = QLabel("Nummer 3", self)


        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: yellow")
        label3.setStyleSheet("background-color: green")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)    

        central_widget.setLayout(vbox)
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()