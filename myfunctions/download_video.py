import youtube_dl

def download_video(url):
    try:
      ytd = youtube_dl.YoutubeDL()
      ytd.download([url])
    except:
        print("unable to download")