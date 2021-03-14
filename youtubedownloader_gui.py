
import youtube_dl, os, sys
from PyQt5 import QtWidgets, uic

ytd = youtube_dl.YoutubeDL()


#take input from user to get URL
def read_input():
    url = window.lineEdit.text()
    url = [url]
    print(url)
    
    #change downloads designation folder
    environment_variables = dict(os.environ)
    homepath = environment_variables['HOMEPATH']
    downloads_folder = ('c:%s\\downloads' % homepath)
    os.chdir(downloads_folder)

    #download video        
    ytd.download(url)

    #hide original button and text
    window.pushButton.hide()
    window.lineEdit.hide()
    window.label.setText("Finished!") #change the label from "" to display finished

    
    



#loading the pyqt application
app = QtWidgets.QApplication([])
window = uic.loadUi("ytdgui.ui")

#setting actions for button clicks
window.pushButton.clicked.connect(read_input)
window.pushButton_2.clicked.connect(sys.exit)


#calling the application
window.show()
app.exec()
