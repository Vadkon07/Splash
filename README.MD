# NOTE

Thir repository needs a lot of help. Thank you for help!

Also this Readme should be edited, because he is copied. from NON-GUI version of this app

For now works only MP3 download function.

#Youtube Downloader

This GUI aplication allows you to download YouTube videos or audio quickly and easily. While many websites offer similar services, they often take more time and include ads. With this app, you can download content directly from YouTube, saving both time and hassle! I personally use it for my beatmaking hobby, because it's very comfortable and fast to download samples from YouTube which then I can use for my melodies.

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration.
3. **Fast Downloading:** Quickly download videos or audio with minimal delay.
4. **GUI** Run the script and be happy to use him with GUI.
5. **Choose Quality:** Bad internet or 4K resolution of video is too good for your 720p monitor? You can choose any quality of video which you want to download.
6. **Offline Audio Extracting:** To download a video app will use internet, but to extract audio it will not use any data.

## Prerequisites

## PC Requirements

Work fine and very fast on any PC, but when program had to [ExtractAudio] from 2 hours long video, it took maybe ~5 minutes. Sounds not attractive, right? But just know that at all my laptop is very old and even can't normally open YouTube itself, so that's a perfect result I think.

Before running the script, make sure you have the following installed:
- **yt-dlp:** Install via pip with the command `pip install yt-dlp`. That's s command-line program to download videos from YouTube and other sites. 
- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.

## How to use

1. Run the script in your terminal or command prompt.
2. Paste the link to your YouTube video when prompted.
3. Choose your download option:
- Enter '**1**' to download audio (MP3):
- Enter '**2**' to download video (MP4)
    - Select a video quality preset:
        - **1** for worst quality
        - **2** for 480p resolution
        - **3** for 720p resolution
        - **4** for the best quality
- Enter '**3**' to download both audio and video
4. Specify the download location path where the files will be saved. Leave blank to download in current directory.
5. The script will process and download the file(s) according to your choices.

## To-Do

- [X] Add possibility to choose quality (by default it's the highest).
- [ ] **Add Support for playlists:** Enable downloading entire YouTube playlists.
- [X] **Error Handling:** Improve error messages for common issues (e.g., invalid URLs, network errors).
- [X] **GUI Version:** Develop a graphical user interface for users who prefer not to use the terminal.
- [X] **Improve Indicator of Download:** For now it looks for a little messy, probably we have to hide output from yt-dlp and create our own output.

## License

This project is licensed under the [MIT License](./LICENSE).
