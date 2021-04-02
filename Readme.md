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
> pip install pyqt5

#### QT Designer

To convert .ui files generated from QT Designer into .py in the command line type:
> filespyuic5 -x ytdgui.ui -o test.py

##  Known bugs:

> if downloading a playlist app seems to hang not letting the user know what its doing in the background, ordering is right but for some reason youtube_dl is operating out of turn
> app trys to change working directory to a windows path

### tests  
> TODO: import asynchio module and see if i can have the proccess of title change and youtube scraping at the same time
> TODO: Research other youtube modules
> TODO: create an elif statement to deal with linux crashes or see if there is a better env variable

### potential remedies
> switch to asynch functions 
> other module
> create elif statement
> env variable


## To-Do

- add an advanced tab so that you can pick download quality and an audio only option
- add a progress bar
