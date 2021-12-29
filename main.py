import yt_dlp as ytdl
import os, sys

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f"C:/Users/slok1/Desktop/Songs/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with ytdl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(["https://www.youtube.com/playlist?list=PLPKA8OH9NAHu8iXKd28AFqiPQe5xqbIDJ"])
