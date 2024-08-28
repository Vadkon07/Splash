print("Running app. Wait some seconds...")

import yt_dlp
import os

url = input("Enter YouTube video URL: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    title = info_dict.get('title', None)

print(f"\nVideo found: {title}")
print("1. Download MP3")
print("2. Download MP4")
print("3. Download both")

ask = input("Enter your choice: ")

if ask == '2' or ask == '3':
    print("\nSelect quality (leave blank for default highest quality):")
    print("1. Low")
    print("2. Medium (up to 480p)")
    print("3. High (up to 720p)")
    print("4. Highest (default)")
    quality_choice = input("Enter quality choice: ")

    if quality_choice == '1':
        quality_format = 'worst[height<=240]+worstaudio'  
    elif quality_choice == '2':
        quality_format = 'bestvideo[height<=480]+bestaudio/best[height<=480]'  
    elif quality_choice == '3':
        quality_format = 'bestvideo[height<=720]+bestaudio/best[height<=720]'  
    else:
        quality_format = 'bestvideo+bestaudio/best'
else:
     quality_format = 'bestvideo+bestaudio/best'


# Ask user for download location
download_location = input("\nEnter download location (leave blank for current directory): ")

if not download_location:
    download_location = os.getcwd()  
else:
    # Ensure the directory exists
    if not os.path.exists(download_location):
        os.makedirs(download_location)

if ask == '1':
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
elif ask == '2':
    ydl_opts = {
        'format': quality_format,  
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4' 
    }
elif ask == '3':
    ydl_opts = {
        'format': quality_format,  
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'keepvideo': True  # Keep the video file after downloading
    }

# Download the selected media
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    
if ask == '3':
    for file in os.listdir(download_location):
        if file.endswith('.webm'):
            os.remove(os.path.join(download_location, file))

print(f"{title} downloaded to {download_location}!")
