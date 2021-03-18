
import youtube_dl, os, sys
from PyQt5 import QtWidgets, uic

ytd = youtube_dl.YoutubeDL()


#take input from user to get URL
#def read_input():
    #url = window.lineEdit.text()
    #url = [url]
    #print(url)
    
    #window.lineEdit.clear()

    #change downloads designation folder
    #environment_variables = dict(os.environ)
    #homepath = environment_variables['HOMEPATH']
    #downloads_folder = ('c:%s\\downloads' % homepath)
    #os.chdir(downloads_folder)

    
    
    #download video        
   #ytd.download(url)
   #ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    #info = ydl.extract_info(url[0], download=False)
    #title = info["title"]


    #hide original button and text
    #window.pushButton.hide()
    #window.lineEdit.hide()






    #window.label.setText("Finished downloading " + title) #change the label from "" to display finished
    #window.label.adjustSize()
    
    



#loading the pyqt application
app = QtWidgets.QApplication([])
window = uic.loadUi("test.ui")

#setting actions for button clicks
#window.pushButton.clicked.connect(read_input)
#window.pushButton_2.clicked.connect(sys.exit)


#calling the application
window.show()
app.exec()
