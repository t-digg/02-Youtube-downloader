from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 600, 200)
    win.setWindowTitle("Youtube Downloader")

    label = QtWidgets.QLabel(win)
    label.setText("My First Label")
    label.move(50,50)
    
    win.show()
    sys.exit(app.exec_())

window()