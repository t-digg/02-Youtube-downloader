# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'YouTubeDownloader2.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.2

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os, youtube_dl


class Ui_YT_Downloader(object):
    def setupUi(self, YT_Downloader):
        YT_Downloader.setObjectName("YT_Downloader")
        YT_Downloader.resize(728, 189)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        YT_Downloader.setPalette(palette)
        YT_Downloader.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(YT_Downloader)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 216, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 216, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Title.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAutoFillBackground(True)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.verticalLayout_2.addWidget(self.Title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.URL_Bar = QtWidgets.QLineEdit(self.frame)
        self.URL_Bar.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.URL_Bar.setFont(font)
        self.URL_Bar.setAlignment(QtCore.Qt.AlignCenter)
        self.URL_Bar.setObjectName("URL_Bar")
        self.horizontalLayout.addWidget(self.URL_Bar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Download_Button = QtWidgets.QPushButton(self.frame)
        self.Download_Button.setMinimumSize(QtCore.QSize(124, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Download_Button.setFont(font)
        self.Download_Button.setObjectName("Download_Button")
        self.verticalLayout.addWidget(self.Download_Button)
        self.Exit_Button = QtWidgets.QPushButton(self.frame)
        self.Exit_Button.setMinimumSize(QtCore.QSize(124, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Exit_Button.setFont(font)
        self.Exit_Button.setObjectName("Exit_Button")
        self.verticalLayout.addWidget(self.Exit_Button)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.Status = QtWidgets.QLabel(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 216, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 216, 58))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.Status.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Status.setFont(font)
        self.Status.setAutoFillBackground(True)
        self.Status.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Status.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Status.setLineWidth(1)
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setWordWrap(True)
        self.Status.setObjectName("Status")
        self.verticalLayout_3.addWidget(self.Status)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        YT_Downloader.setCentralWidget(self.centralwidget)

        self.retranslateUi(YT_Downloader)
        self.URL_Bar.returnPressed.connect(self.Download_Button.click)
        self.Download_Button.clicked.connect(self.Download_Click)
        self.Exit_Button.clicked.connect(YT_Downloader.close)
        QtCore.QMetaObject.connectSlotsByName(YT_Downloader)

    def retranslateUi(self, YT_Downloader):
        _translate = QtCore.QCoreApplication.translate
        YT_Downloader.setWindowTitle(_translate("YT_Downloader", "Youtube Downloader"))
        self.Title.setText(_translate("YT_Downloader", "YouTube Downloader"))
        self.URL_Bar.setPlaceholderText(_translate("YT_Downloader", "Enter YouTube URL here"))
        self.Download_Button.setText(_translate("YT_Downloader", "Download"))
        self.Exit_Button.setText(_translate("YT_Downloader", "Exit"))
        self.Status.setText(_translate("YT_Downloader", "Please Enter YouTube video URL or playlist URL above"))

    def Download_Click(self, YT_Downloader):
        url = self.URL_Bar.text()
        self.URL_Bar.clear()

        def get_title(url):
            
            #added try/except in order to bounce out bad URLs and avoid app crashes
            try:
                ytd = youtube_dl.YoutubeDL()
                data = ytd.extract_info(url, download=False)
                title = data["title"]
                
                return title
            
            except:
                self.Status.setText("Couldn't find requested video please try again.")
        
        
        # Calling the function to get the title of the video requested
        title = get_title(url)
        self.Status.setText(f"Downloading: {title}")
    
        environment_variables = dict(os.environ)
        homepath = environment_variables['HOMEPATH']
        downloads_folder = ('c:%s\\downloads' % homepath)
        os.chdir(downloads_folder)
        
        #Select destignation folder
        
        def launchDialog(url):
            
            
           
            try:   
                selected_folder = QFileDialog.getExistingDirectory(caption='Select a folder')
                os.chdir(selected_folder)
                download_video(url)  
            except:
                self.Status.setText("Download Canceled")
                
            
            
        
            
                

        
       
        

        ##change downloads designation folder
        #environment_variables = dict(os.environ)
        #homepath = environment_variables['HOMEPATH']
        #downloads_folder = ('c:%s\\downloads' % homepath)
        #os.chdir(downloads_folder)

        
        # added a try/except statement to avoid crashes
        def download_video(url):
            print(url)
            


            try:
                
                url = [url]
                ytd = youtube_dl.YoutubeDL()
                ytd.download(url)
                self.Status.setText(f"Downloaded {title}")
            except:
                self.Status.setText("Couldn't find requested video please try again.")

          
        launchDialog(url)    
        

            
        
        
        
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YT_Downloader = QtWidgets.QMainWindow()
    ui = Ui_YT_Downloader()
    ui.setupUi(YT_Downloader)
    YT_Downloader.show()
    sys.exit(app.exec_())
