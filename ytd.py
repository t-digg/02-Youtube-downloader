import youtube_dl, os

ytd = youtube_dl.YoutubeDL()

#get URL from user
link = input('Please enter the URL of the video or playlist you wish to download: ')
link = [link] #can be a list of multiple links

#change directory to downloads folder
environment_variables = dict(os.environ)
homepath = environment_variables['HOMEPATH']
downloads_folder = ('c:%s\\downloads' % homepath)
os.chdir(downloads_folder)

#downloads video to current directory 
ytd.download(link)
