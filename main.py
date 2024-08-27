print("Running app. Wait some seconds...")

import yt_dlp

url = input("Enter YouTube video URL: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    title = info_dict.get('title', None)

print(f"\nVideo which we found: {title}")
print("1. Download MP3")
print("2. Download MP4")
print("3. Download both")

ask = input("Enter your choice: ")

if ask == '1':
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
elif ask == '2':
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4'
    }
elif ask == '3':
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"{title} downloaded!")

