import yt_dlp

url = "https://www.youtube.com/watch?v=LWnrRXUk0gg&t"

ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best[height=1080]',
    'outtmpl': 'video.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(yt_dlp.__file__)
