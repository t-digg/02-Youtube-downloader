from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#creating a subclass of qmain window
class MyWindow(QMainWindow):

    #sets size, position, and title of window
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 600, 200)
        self.setWindowTitle("Youtube Downloader")
        self.initUI()
    
    #defines label and button aspects of ui
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("My First Label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.button_click)
    
    #changes label's text when button is clicked
    def button_click(self):
        self.label.setText("you pressed the button")
        self.update()
    
    #refits label size
    def update(self):
        self.label.adjustSize()

#runs the program
def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

#calls the function
window()