import youtube_dl

link = ['https://www.youtube.com/watch?v=6LzuIch-wQo&list=PLG49S3nxzAnmpdmX7RoTOyuNJQAb-r-gd&index=2']

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)
