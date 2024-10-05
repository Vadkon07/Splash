<p align="center">
  <img src="VideoXYZ_logo.png" alt="App Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-green"/>
</p>

# VideoXYZ

This GUI application allows you to download **YouTube videos** or **audio** quickly and easily. While many websites offer similar services, they often take more time and include ads. With **VideoXYZ**, you can download content directly from **YouTube**, saving both time and hassle! I personally use it for my beatmaking hobby, because it's very convenient and fast to download samples from **YouTube**, which I then use for creating melodies.

You can download videos in any quality, from 144p and up to 4k!

**You downloaded some music with VideoXYZ and want to listen to her? Try to do it in our another project [Style Music Player](https://github.com/Vadkon07/Style_Music_Player)!**

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration. Clone and run!
3. **Fast Downloading:** Quickly download videos or audio with minimal delay. On 99% speed if download depends from your PC specifications and speed of internet.
4. **User-Friendly GUI**: Easy-to-use graphical interface for a more intuitive experience. Our app has plenty amount of useful GUI features, which make this app very easy to use even for kids. Some examples: progress bars, a lot of different notifications about changes in app which you do, notifications about new updates (which of course can be installed automaticall).
5. **Choose Quality:** Select the video quality that best suits your needs, from low resolution to 4K. Low resolutions are useful for people which have not a very stable internet, small amount of free storage, low-end computer, or just will be runnerd on a small diplays.
6. **Offline Audio Extraction:** The app downloads videos using the internet but extracts audio offline, saving bandwidth. We are using ffmpeg, a very powerful tool which use every professinal which works a lot with audio/video.
7. **Terminal-Based Version Available:** A command-line (outdated)  version of the app is also available in [one of my repositories](https://github.com/Vadkon07/YouTube_Downloader), offering slightly different functionalities. She is pretty outaded for now, but still should work fine. This version will be useful if your computer doens't has a window manager (in two words - for servers).
8. **Optimised for low resolution monitors:** I know that a lot of people continue to use their ThinkPads etc. from 2004 or even older, so I decided to optimise this app for theirs displays. This app should work fine and not take a lot of space on your monitor even if he has only a 640x320 display resolution. On i3 manager you even can change a size of any window which this app will show to you, but I'm not sure about other window managers.
9. **Themes:** Our app has white, black, lime, purple, and pink themes. You can share your own themes with us! Soon we will try to add a gradient themes, which will significanty improve appearance of our app. Also it will be cool to add some custom styled themes as desert, sea, etc.
10. **Sounds:** We have a sound which will notificate you about finished downloading of your files. Soon we also will add some settings for sounds, like custom sounds etc. Also you can enable/disable all sounds inside setting of this app. All sounds which we have in our app are created by myself, by using DAW applications.
11. **Playlists Support:** You can download a full album of your favorite artist in one click!
12. **Regular Updates:** This app is always up to date, so you can never care about her availability. After clone of this app you will see information about changes in last update.
13. **Notifications:** We will send to you a notification if it will be available a newer version of this app.

## Prerequisites

Before running the script, make sure you have the following installed:

- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.
- **PyQt6, yt_dlp, pyqtdarktheme:** To install run `pip install -r requirements.txt`.
- **Pygame:** We use him for sounds.

## PC Requirements

Here's **recommended** PC specifications:

- **OS:** Linux, Windows, MacOS
- **RAM:** 1GB+
- **CPU:** Intel Pentium 4 or higher
- **GPU:** Just to download a file you don't need GPU, but to do some conversions of **10 minute 1080p** video from one format to another it will be enough something in a kind of Intel UHD630. For **1 hour+ 4k** video processing of course it's better to have a powerful external GPU.
- **Storage:** 500MB (app itself and her packages)

## How to use

1. Run the script in your terminal or command prompt.
2. Paste the link to your YouTube video when prompted.
3. Choose your download option:
- Click '**MP3**' to download audio (MP3):
- Click '**MP4**' to download video (MP4)
    - Select a video quality preset:
        - **Worst** for worst quality (nice for old computer and slow internet)
        - **480p** for 480p resolution
        - **720p** for 720p resolution
        - **Best** for the best quality (usually 1080p or 4k)
- Click '**Both**' to download both audio and video
- Click '**webm**' to download a video in webm format

4. The script will process and download the file(s) in your **(!) currently choosed directory** according to your choices.

## How to read version of this app

**In version 1.9.0.1 (example):**

    1: Major revision (new UI, lots of new features, conceptual change, etc.)

    9: Minor revision (maybe a change to a search box, 1 feature added, collection of bug fixes)

    0: Bug fix release

    1: Build number (if used)—that's why you see the .NET framework using something like 2.0.4.2709

## License

This project is licensed under the [MIT License](./LICENSE).

## To-Do

When we will finish all these tasks - we will release version v1.0.

- [x] **Playlist Support:** Enable downloading of entire YouTube playlists.
- [x] **Better Download Indicator:** Improve the download progress indicator to be more user-friendly, and probably also hide raw output from terminal.
- [x] **More Formats:** Expand the format options beyond MP3 and MP4 to include formats like WAV, OGG, and more.
- [x] **Descriptions and questions on every page:** Like: "Choose a format".
- [x] **Fix progressbar:** Hide progressbar when he is not used.
- [x] **Check Updates:** It should read file from this repository and check is it has a mention of installed version or not, and if not - notificare user about available update. Plan for code: download file ver.html (or json) -> open him and read -> if doesn't contatin mention of installed version - show messagebox about available update. NOTE: I made it even better, so for now it can even download updates automatically!
- [ ] **Support developer with donation of $5:** It will motivate me even more!
</details>

### Last Updated
This README was last updated on **October 5, 2024** for version **v0.9.0**. All new things added in app afer this date + version are **NOT** described/mentioned here.
