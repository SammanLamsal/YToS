from tkinter.constants import CENTER
import yt_dlp as ytdl
import os, sys
import tkinter as tk
from tkinter import filedialog, Text

from yt_dlp.utils import DownloadError


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f"C:/Users/slok1/Desktop/Songs/%(title)s.%(ext)s",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

linkEntry = ""

def downloadSong():
    if(DownloadError):
        canvas.create_text(398, 450, text = "INVALID INPUT, TRY AGAIN")
    with ytdl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([linkEntry.get()])



if __name__ == "__main__":
    root = tk.Tk()
    root.title("YTOS")
    root.geometry("800x800")
    root.resizable(height = None, width = None)

    canvas = tk.Canvas(root, bg = "#263")
    canvas.pack(fill="both", expand="true")
    
    linkEntry = tk.Entry(root, justify=CENTER)
    canvas.create_window(200, 140, window=linkEntry)
    linkEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

    linkText = canvas.create_text(398, 350, anchor = CENTER, text = "INPUT PLAYLIST LINK")

    download = tk.Button(root, text = "DOWNLOAD SONG", padx=10, pady=5, fg="white", bg="#263D42", command = downloadSong)
    download.pack()

    root.mainloop()

