<p align="center">
  <img src="VideoXYZ_logo.png" alt="App Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-green"/>
</p>

# VideoXYZ

This GUI application allows you to download **YouTube videos** or **audio** quickly and easily. While many websites offer similar services, they often take more time and include ads. With **VideoXYZ**, you can download content directly from **YouTube**, saving both time and hassle! I personally use it for my beatmaking hobby, because it's very convenient and fast to download samples from **YouTube**, which I then use for creating melodies.

You can download videos in any quality, from 144p and up to 4k!

**You downloaded some music with VideoXYZ and want to listen to her? Try to do it in our another project [Style Music Player](https://github.com/Vadkon07/Style_Music_Player) !

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration. Clone and run!
3. **Fast Downloading:** Quickly download videos or audio with minimal delay.
4. **User-Friendly GUI**: Easy-to-use graphical interface for a more intuitive experience. During downloading of file you also will see a progress bar.
5. **Choose Quality:** Select the video quality that best suits your needs, from low resolution to 4K.
6. **Offline Audio Extraction:** The app downloads videos using the internet but extracts audio offline, saving bandwidth.
7. **Terminal-Based Version Available:** A command-line (outdated)  version of the app is also available in [one of my repositories](https://github.com/Vadkon07/YouTube_Downloader), offering slightly different functionalities.
8. **Optimised for low resolution monitors:** I know that a lot of people continue to use their ThinkPads etc. from 2004 or even older, so I decided to optimise this app for theirs displays. This app should work fine and not take a lot of space on your monitor even if he has only a 640x320 display resolution.
9. **Black and white themes:** Also in the future we will add different custom themes as lime, pink, and purple!
10. **Sounds:** We started to add different sounds in our app. For now we have a sound which will notificate you about finished downloading of your files. Soon we also will add some settings for sounds.

## Prerequisites

Before running the script, make sure you have the following installed:

- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.
- **PyQt6,yt_dlp,pyqtdarktheme:** To install run `pip install -r requirements.txt`.
- **Pygame:** We use him for sounds.

## PC Requirements

Here's recommended PC specifications:

- **OS:** Linux, Windows, MacOS
- **RAM:** 1-2GB
- **CPU:** Intel Pentium 4 or higher
- **GPU:** Just to download a file you don't need GPU, but to do some conversions of **10 mins 1080p** videos from one format to another it will be enough something in a kind of Intel UHD630. For **1 hour+ 4k** video processing of course you should have a powerful GPU.
- **Storage:** 500MB (app itself and her packages)

## How to use

1. Run the script in your terminal or command prompt.
2. Paste the link to your YouTube video when prompted.
3. Choose your download option:
- Click '**MP3**' to download audio (MP3):
- Enter '**MP4**' to download video (MP4)
    - Select a video quality preset:
        - **Worst** for worst quality (nice for old computer and slow internet)
        - **480p** for 480p resolution
        - **720p** for 720p resolution
        - **Best** for the best quality (usually 1080p or 4k)
- Enter '**Both**' to download both audio and video
4. The script will process and download the file(s) in your **currently choosed directory** according to your choices.

## How to read version of app

**In version 1.9.0.1 (example):**

    1: Major revision (new UI, lots of new features, conceptual change, etc.)

    9: Minor revision (maybe a change to a search box, 1 feature added, collection of bug fixes)

    0: Bug fix release

    1: Build number (if used)—that's why you see the .NET framework using something like 2.0.4.2709

## License

This project is licensed under the [MIT License](./LICENSE).

<details>
	<summary>To-Do</summary>

When we will finish all these tasks - we will release version v1.0.

- [ ] **Playlist Support:** Enable downloading of entire YouTube playlists.
- [ ] **Better Download Indicator:** Improve the download progress indicator to be more user-friendly, and probably also hide raw output from terminal.
- [ ] **More Formats:** Expand the format options beyond MP3 and MP4 to include formats like WAV, OGG, and more.
- [ ] **Descriptions and questions on every page:** Like: "Choose a format".

</details>

### Last Updated
This README was last updated on **September 15, 2024**. All new things added in app afer this date are **NOT** described here.
