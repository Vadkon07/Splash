<p align="center">
  <img src="Splash_Logo_S.png" alt="App Logo"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LICENSE-MIT-green"/>
</p>

# ***Splash***

This GUI application allows you to download **images**, **videos** or **audio** from a lot of social media or any website at all quickly and easily. While many websites offer similar services, they often take more time and include ads. With **Splash**, you can download content directly from litearlly any popular social media, saving both time and hassle! I (Vadim Kondratov, nice to meet you!) personally use it for my beatmaking hobby, because it's very convenient and fast to download samples from **YouTube**, which I then use for creating melodies.

You can download videos in any quality, from 144p and up to 4k!

**You downloaded some music with** ***Splash*** **and want to listen to her? Try to do it in our another project named [Style Music Player](https://github.com/Vadkon07/Style_Music_Player)!**

## **Why I should install Splash instead of just using online downloaders?**

In ***Splash*** you will always have the best quality of downloaded files, while literally every second online converter do something in a kind of compression or just doesn't show to you the best quality download option, and it will reduce quality of file. Splash doesn't do it, so he will give to you the highest available quality always. Also in Splash you have a lot of different settings, which will significanlty improve your experience with app.

This app download a file from internet and then works a lot on his conversion. So it's not just a downloader, it's also a converter.

## Features
1. **Ad-free:** Enjoy a seamless experience without interruptions.
2. **No API Needed:** Download directly without the need for any API keys or extra configuration. Clone and run!
3. **Fast Downloading:** Quickly download videos or audio with minimal delay. On 99% speed if download depends from your PC specifications and speed of internet.
4. **User-Friendly GUI**: Easy-to-use graphical interface for a more intuitive experience. Our app has plenty amount of useful GUI features, which make this app very easy to use even for kids. Some examples: progress bars, a lot of different notifications about changes in app which you do, notifications about new updates (which of course can be installed automaticall).
5. **Choose Quality:** Select the video quality that best suits your needs, from low resolution to 4K. Low resolutions are useful for people which have not a very stable internet, small amount of free storage, low-end computer, or just will be runnerd on a small diplays.
6. **Offline Audio Extraction:** The app downloads videos using the internet but extracts audio offline, saving bandwidth. We are using ffmpeg, a very powerful tool which use every professinal which works a lot with audio/video.
7. **Terminal-Based Version Available:** A command-line (outdated) version of the app is also available in [one of my repositories](https://github.com/Vadkon07/YouTube_Downloader), offering slightly different functionalities. She is pretty outaded for now, but still should work fine. This version will be useful if your computer doens't has a window manager (servers).
8. **Optimised for low resolution monitors:** I know that a lot of people continue to use their ThinkPads etc. from 2004 or even older, so I decided to optimise this app for theirs displays. This app should work fine and not take a lot of space on your monitor even if he has only a 640x320 display resolution. On i3 manager you even can change a size of any window which this app will show to you, but I'm not sure about other window managers.
9. **Themes:** Our app has white, black, lime, purple, and pink themes. You can share your own themes with us! Soon we will try to add a gradient themes, which will significanty improve appearance of our app. Also it will be cool to add some custom styled themes as desert, sea, etc.
10. **Sounds:** We have a sound which will notificate you about finished downloading of your files. Soon we also will add some settings for sounds, like custom sounds etc. Also you can enable/disable all sounds inside setting of this app. All sounds which we have in our app are created by myself, by using DAW applications.
11. **Playlists Support (YouTube):** You can download a full album of your favorite artist in one click!
12. **Regular Updates:** This app is always up to date, so you can never care about her availability. We will notificate you about new available updates every time when you run this app.
13. **Notifications:** We will send to you a notification if it will be available a newer version of this app. If you decided to download a 5-hour 4K video of dancing cats from YouTube, it can take pretty a lot of time. And in order to make you free from waiting and checking your screen every 3 seconds I added in this app a notification sound, which will notificate you about completed downloading in the end. Don't forget to turn on a sound on your computer and inside app's settings!
14. **Resources Monitor:** You can always know how busy your PC is. By this monitor you can read how many percent of your RAM or CPU power are filled, and by it you can understand what caused slow conversion or download. Engine of this app I copied from another my project [EasyBench](https://github.com/Vadkon07/EasyBench).
15. **Compatible with old computers:** It should work fine even if you have a very old computer. I own a very old laptop with AMD E-300 processor, so I always care about people which are in the same situaiton with me.
16. **Search History (BETA):** After each search app saves your video/audio which she found inside her database, and then in **Settings** menu you can check and clean (soon) history.
17. **Multiple Downloads:** In **Main** you can run also another window (or even thousands of them), and by it you can download a lot of files in one time. It's useful if you want to download two or more different files in one moment, but probably it will use your CPU more and also split your internet on two tasks.

> [!WARNING]
> I develop this app only on my Linux laptop, so I can't give to you any warranties that it will work the same on Windows. Maybe it can have some weird things in GUI, so if you will notice any bugs, please - send me an email with screenshot(s).

## Prerequisites

Before running the app, make sure you have the following installed:

- **ffmpeg:** Ensure ffmpeg is installed on your machine for video/audio processing.
- **PyQt6, yt_dlp, pyqtdarktheme:** The most important things here! GUI and engine.
- **Pygame:** We use him for sounds.
- **Psutil:** Necessary for Resources Monitor.

## How to install ***Splash***

1. Clone this repository:

> git clone https://github.com/Vadkon07/Splash

2. Open directory with installed repository and install requirements:

> pip install -r requirements.txt

> [!NOTE]
> Once I was trying to install this app on Windows, but I got some errors which told me to install **Visual C++ 14**, so you will also have to do it if you are a Windows user.

3. Run app:

> python main.py

## PC Requirements

Here's **recommended** PC specifications:

- **OS:** Linux, Windows, MacOS, FreeBSD
- **RAM:** 1GB+
- **CPU:** Intel Pentium 4 or higher
- **GPU:** Just to download audio you don't need GPU, but to do some conversions of **10 minute 1080p** video from one format to another it will be enough something in a kind of Intel UHD630. For **1 hour+ 4k** video processing of course it's better to have a powerful external GPU.
- **Storage:** 500MB (app itself and her packages)

> [!IMPORTANT]
> You can download whatever you need even on a Pentium 3, but keep in your mind that it will take much more time than on a pretty cheap Intel Core i3 2-3'th Gen.

## How to use

1. Run the script in your terminal or command prompt.
2. Paste the link to your YouTube video when prompted.
3. Choose your download option:
- Click '**MP3**' to download audio (MP3):
- Click '**WAV**' to download audio (WAV):
- Click '**MP4**' to download video (MP4)
    - Select a video quality preset:
        - **Worst** for worst quality (nice for old computer and slow internet)
        - **480p** for 480p resolution
        - **720p** for 720p resolution
        - **Best** for the best quality (usually 1080p or 4k)
- Click '**Both**' to download both audio and video
- Click '**webm**' to download a video/audio in webm format

4. The script will process and download the file(s) in your **(!) currently choosed directory** according to your choices.

## How to read version of this app

**In version 1.9.0.1 (example):**

    1: Major revision (new UI, lots of new features, conceptual change, etc.)

    9: Minor revision (maybe a change to a search box, 1 feature added, collection of bug fixes)

    0: Bug fix release (fix something what was wrong in code, improve align of image, etc.)

    1: Build number (if used)—that's why you see the .NET framework using something like 2.0.4.2709

## License

> This project is licensed under the [MIT License](./LICENSE).

## To-Do to release version 2.0

- [x] **Make compatible with other popular social media:** Instagram, Twitter, etc. Add possibility just to download posts or audio from them. Make this app universal!
- [x] **Change requirements.txt:** It doesn't include all packages which should be installed. We have to solve it!
- [x] **Make code more readable:** It will be better to reorganise defs and add/remove spaces in code.
- [x] **Hide custom menu:** Menu bar takes some place, and to get more free space in our app it will be nice to add an arrow which will hide/show this menu. UPDATED: Hm, it's better just to make it for a little smaller.
- [x] **Add resources monitor:** I have a nice project named **EasyBench**, which was created to benchmark your computer. I think that I can copy from his code some things as CPU, RAM, GPU resource monitors and integrate them inside VideoXYZ. It will show usage of computer's resources while using VideoXYZ in terminal or another window, to make it easier for user to understand how busy his computer is. Also I will add possibility to turn it ON or OFF in DEV menu. NOTE: Now it has only RAM and CPU monitor, but we also have to add one monitor for GPU. Also it doens't work in background, and it also should be solver.
- [x] **Better Thumbnail Window:** For now it just open thumbnail in a new window, but what if instead it will show small thumbnail near "Choose a format"?
- [x] **Sound ON/OFF:** Replace it with 'Enable Sound' and 'Disable Sound'. It should read this setting from json and set a needed text. Like, it's already added, but doens't work.
- [x] **More sounds + settings for them:** It will be nice to add something in a kind of themes for sounds, and also make it possible to change them.
- [ ] **Make repository more organised:** Sort files in public, src, etc.
- [ ] **More formats:** as AAC etc.

## FAQ

**Q:** How much time it will take to install this app?
**A:** You just clone repository and then run 'pip install -r requirements.txt', and then everything depends from your internet connection. For me it took less than 5 minutes on my pretty old laptop.

**Q:** Is there any kind of tracking of me when I use this app?
**A:** No, we just don't need it.

**Q:** Is this app is free to use?
**A:** Yes, this app is fully free and you will never need to pay to use her.

**Q:** How can I help developers of this app?
**A:** You have a lot of different ways to do it. At first the best help for us it's just to help us with development (bug fixes, new ideas, etc), but also you can help our developers with donations (open profile of a very active developer of this app and find a donation link)

**Q:** What if I got some errors while using the app and can't solve it?
**A:** Open new issue and our community will try to help you. At all at first try just to reinstall this app.

> [!NOTE]
> At this moment I create this app fully alone, literally without any help. It will be nice to have a command of 2-3 people, just to work on our app faster. I go to school and have a busy schedule, so I'm not able to code all day long, especially because at home I have some problems with internet connection. So, I'm always ready to start to work on this app together with you!

### Last Updated
> This README was last updated on **October 29, 2024** for version **v1.5.0**. All new things added in app afer this date + version are **NOT** described/mentioned here.
