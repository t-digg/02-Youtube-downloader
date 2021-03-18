# Readme

- The purpose of this project is to be able to download youtube videos automatically from a youtube playlist or video using python.
- In the proccess of building this app I will be learning python, 3rd party modules, pyqt5 designer, git/github, markdown language, and documentation.



## 3rd party modules/tools

### youtube-dl 

To install package from command line enter:

> pip install youtube_dl

Github repo: https://github.com/ytdl-org/youtube-dl

### pyqt5 

To install package from command line enter:
>pip install pyqt5

#### QT Designer

To convert .ui files generated from QT Designer into .py in the command line type:
> filespyuic5 -x ytdgui.ui -o test.py

##  Known bugs:

### status label does not update even though it's placed logically above the YouTube downloader itself

#### tests  
- attempted to change position of the changing of the underlying qlabel - **fail**
- attempted to take out youtube downloader to see if qlabel would set - **pass** -m "Likely a problem within youtube downloader 
- took out directory change- **fail**
- tried to *hide()* initial qlabel and *show()* qlabel - **fail**
- tried beginning with blank string q-label then changing qlabel **fail**
- 
#### potential remedies
- write a function seperate for the download/path change to execute after the *Download_Click* function
- create a progress bar from the youtube_dl function?
- add a third label that is hidden until button push