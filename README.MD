# Youtube Downloader

This GUI application allows you to download YouTube videos or audio quickly and easily. While many websites offer similar services, they often take more time and include ads. With this app, you can download content directly from YouTube, saving both time and hassle! I personally use it for my beatmaking hobby because it's very convenient and fast to download samples from YouTube, which I then use for creating melodies.

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration.
3. **Fast Downloading:** Quickly download videos or audio with minimal delay.
4. **User-Friendly GUI**: Easy-to-use graphical interface for a more intuitive experience.
5. **Choose Quality:** Select the video quality that best suits your needs, from low resolution to 4K.
6. **Offline Audio Extraction:** The app downloads videos using the internet but extracts audio offline, saving bandwidth.
7. **Terminal-Based Version Available:** A command-line version of the app is also available in [one of my repositories](https://github.com/Vadkon07/YouTube_Downloader), offering slightly different functionalities.

## Prerequisites

Before running the script, make sure you have the following installed:

- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.
- **PyQt6,yt_dlp,pyqtdarktheme:** To install run `pip install -r requirements.txt`.

## PC Requirements

The app works well on any PC. However, note that for certain operations, such as extracting audio from a two-hour-long video, it may take some time (approximately 5 minutes on an older machine). This performance is quite impressive given that my laptop is very old and struggles to open YouTube itself.

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

- [ ] **Quality Selection:** Allow users to choose the video quality (currently, it defaults to the highest available quality).
- [ ] **Playlist Support:** Enable downloading of entire YouTube playlists.
- [ ] **GUI Improvements:** Optimize the dark theme and add a button to switch themes.
- [ ] **Better Download Indicator:** Improve the download progress indicator to be more user-friendly and hide the raw output from `yt-dlp`.
- [ ] **More Formats:** Expand the format options beyond MP3 and MP4 to include formats like WAV, OGG, and more.
- [ ] **Download Both Audio and Video:** Enhance the app to allow simultaneous downloading of both audio and video.
- [ ] **Settings Menu:** Add a settings menu for theme selection and other configurations.
- [ ] **Improve README:** Make this README more comprehensive and user-friendly.
- [ ] **Return to Start on Completion:** After a download is finished, return the user to the initial screen to enter a new link.
- [ ] **User Notifications:** Add clear notifications for users about ongoing downloads, rather than displaying raw terminal output.

## How to read version of app

**In version 1.9.0.1 (example):**

    1: Major revision (new UI, lots of new features, conceptual change, etc.)

    9: Minor revision (maybe a change to a search box, 1 feature added, collection of bug fixes)

    0: Bug fix release

    1: Build number (if used)—that's why you see the .NET framework using something like 2.0.4.2709

## License

This project is licensed under the [MIT License](./LICENSE).
