import yt_dlp
import os
import sys

print("Running app. Wait some seconds...")

# Function to print error messages
def print_error(message):
    print(f"Error: {message}")

# Function to print progress messages
def print_progress(message):
    print(f"{message}", end="\r")  # Overwrite the line

# Get URL from user
url = input("Enter YouTube video URL: ")

# Extract video info
try:
    with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        title = info_dict.get('title', None)
        if not title:
            raise ValueError("Unable to retrieve video title.")
except Exception as e:
    print_error(f"Failed to retrieve video information: {e}")
    exit(1)

print(f"\nVideo found: {title}")
print("1. Download MP3")
print("2. Download MP4")
print("3. Download both")

ask = input("Enter your choice: ")

# Determine quality format based on user's choice
if ask in ['2', '3']:
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
    try:
        if not os.path.exists(download_location):
            os.makedirs(download_location)
    except Exception as e:
        print_error(f"Failed to create directory: {e}")
        exit(1)

# Set download options based on user's choice
if ask == '1':
    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,  # Suppress yt-dlp output
        'progress_hooks': [lambda d: print_progress("|Downloading MP3...") if d['status'] == 'downloading' else None]
    }
elif ask == '2':
    ydl_opts = {
        'format': quality_format,
        'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'quiet': True,  # Suppress yt-dlp output
        'progress_hooks': [lambda d: print_progress("|Downloading MP4...") if d['status'] == 'downloading' else None]
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
        'keepvideo': True,  # Keep the video file after downloading
        'quiet': True,  # Suppress yt-dlp output
        'progress_hooks': [lambda d: print_progress("|Downloading both MP3 and MP4...") if d['status'] == 'downloading' else None]
    }

# Download the selected media
try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    # Clean up extra video files if downloading both audio and video
    if ask == '3':
        for file in os.listdir(download_location):
            if file.endswith('.webm'):
                os.remove(os.path.join(download_location, file))
    
    print(f"{title} downloaded to {download_location}!")
except Exception as e:
    print_error(f"Failed to download the video: {e}")
    exit(1)
