# NOTE

This repository needs a lot of work. Thank you for your help!

# Youtube Downloader

This GUI aplication allows you to download YouTube videos or audio quickly and easily. While many websites offer similar services, they often take more time and include ads. With this app, you can download content directly from YouTube, saving both time and hassle! I personally use it for my beatmaking hobby, because it's very comfortable and fast to download samples from YouTube which then I can use for my melodies.

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration.
3. **Fast Downloading:** Quickly download videos or audio with minimal delay.
4. **GUI** Run the script and be happy to use him with GUI.
5. **Choose Quality:** Bad internet or 4K resolution of video is too good for your 720p monitor? You can choose any quality of video which you want to download.
6. **Offline Audio Extracting:** To download a video app will use internet, but to extract audio it will not use any data.
7. **Terminal-based version:** Also we have a terminal-based version of this app, which you can find inside one of my repositories. Maybe she has for a little different functions.

## Prerequisites

## PC Requirements

Work fine and very fast on any PC, but when program had to [ExtractAudio] from 2 hours long video, it took maybe ~5 minutes. Sounds not attractive, right? But just know that at all my laptop is very old and even can't normally open YouTube itself, so that's a perfect result I think.

Before running the script, make sure you have the following installed:
- **yt-dlp:** Install via pip with the command `pip install yt-dlp`. That's s command-line program to download videos from YouTube and other sites. 
- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.
- **pyqt6:** GUI widgets.

## How to use

1. Run the script in your terminal or command prompt.
2. Paste the link to your YouTube video when prompted.
3. Choose your download option:
- Click '**MP3**' to download audio (MP3):
- Enter '**MP4**' to download video (MP4)
    - Select a video quality preset:
        - **Worst** for worst quality
        - **480p** for 480p resolution
        - **720p** for 720p resolution
        - **Best** for the best quality
- Enter '**Both**' to download both audio and video
4. Specify the download location path where the files will be saved. Leave blank to download in current directory.
5. The script will process and download the file(s) according to your choices.

## To-Do

- [ ] Add possibility to choose quality (by default it's the highest).
- [ ] **Add Support for playlists:** Enable downloading entire YouTube playlists.
- [ ] **Improve GUI:** Optimise dark theme, create a button to add posibiity to change a current theme.
- [ ] **Improve Indicator of Download:** For now it looks for a little messy, probably we have to hide output from yt-dlp and create our own output.
- [ ] **More formats:** Instead of MP3 and MP4 in menu, we can add a Audio and Video, and inside them add a lot of lines where person can choose from formats as mp3, wav, ogg, and for Video the same.
- [ ] **Add Both function:** For now app can download only MP3 or MP4.
- [ ] **Add menu:** Add menu with settings, as **theme** and **exit**.
- [ ] **Make this README better.**
- [ ] **When download is finished move back to the first widget where you have to paste a link.
- [ ] **Add texts which will notificate a user about downloading something, now it only prints his output in terminal.

## License

This project is licensed under the [MIT License](./LICENSE).
