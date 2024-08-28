# Youtube Downloader

This simple script allows you to download YouTube videos or audio quickly and easily. While many websites offer similar services, they often take more time and include ads. With this app, you can download content directly from YouTube, saving both time and hassle!

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration.
3. **Fast Downloading:** Quickly download videos or audio with minimal delay.
4. **Terminal-based:** Run the script directly from your terminal or command prompt.

## Prerequisites

Before running the script, make sure you have the following installed:
- **yt-dlp:** Install via pip with the command `pip install yt-dlp`.
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
- [ ] **Error Handling:** Improve error messages for common issues (e.g., invalid URLs, network errors).
- [ ] **GUI Version:** Develop a graphical user interface for users who prefer not to use the terminal.

## License

This project is licensed under the [MIT License](./LICENSE).
