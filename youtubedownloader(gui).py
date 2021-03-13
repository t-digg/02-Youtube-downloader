
import youtube_dl, os, sys
from PyQt5 import QtWidgets, uic

ytd = youtube_dl.YoutubeDL()


#take input from the lineEdit object in the ui and print it to the console
def read_input():
    url = window.lineEdit.text()
    url = [url]
    print(url)
    
    environment_variables = dict(os.environ)
    homepath = environment_variables['HOMEPATH']
    downloads_folder = ('c:%s\\downloads' % homepath)
    os.chdir(downloads_folder)
        
    ytd.download(url)

    window.pushButton.hide()
    window.lineEdit.hide()
    window.label.setText("Finished!")

    
    




app = QtWidgets.QApplication([])
window = uic.loadUi("ytdgui.ui")

window.pushButton.clicked.connect(read_input)
window.pushButton_2.clicked.connect(sys.exit)

window.show()
app.exec()
