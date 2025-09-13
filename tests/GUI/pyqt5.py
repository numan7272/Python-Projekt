import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GUI Test")
        self.setGeometry(700, 300, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 500, 500)

        pixmap = QPixmap("cleveland-ohio-city-skyline-sunrise-lake-erie-aaron-geraud.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)

       
       
       
       
       
       # self.setWindowIcon(QIcon("profile_pic.png"))
#
       # label = QLabel("Moin", self)
       # label.setFont(QFont("Calibri", 32))
       # label.setGeometry(150, 100 , 200, 200)
       # label.setStyleSheet("color: #0a64ff;" \
       #                     "background-color: #7a4a06;" \
       #                     "font-weight: cursiv;" \
       #                     "font-style: italic;" \
       #                     "text-decoration: underline;")
       # label.setAlignment(Qt.AlignCenter)

       
    
    

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





if __name__ == "__main__":
    main()