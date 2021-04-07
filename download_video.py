from __future__ import unicode_literals
import youtube_dl
ydl_opts = {
    'outtmpl': 'Downloads/%(title)s.%(ext)s',
    'format': 'mp4',
    'writesubtitles': True,
    'subtitleslangs': ['en'],
    'subtitlesformat': 'srv3',
    'skip_download': True,
    'allsubtitles': True
}
url = "https://www.youtube.com/watch?v=Dfo-7GOtEY8"
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
print("Download Successful!")
