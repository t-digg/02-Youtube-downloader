import youtube_dl

def get_title(url):
    
    try:
        ytd = youtube_dl.YoutubeDL()
        data = ytd.extract_info(url, download=False)
        title = data["title"]
        return title
        
    except:
        print("video not found")


