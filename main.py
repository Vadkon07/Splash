import sys
import os
import subprocess
import qdarkstyle
import markdown
import yt_dlp
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QMainWindow, QMenuBar, QTextBrowser, QDialog, QGridLayout, QLabel, QScrollArea, QProgressBar, QGraphicsOpacityEffect
from PyQt6.QtGui import QAction, QImage, QPixmap
from PyQt6.QtCore import QPropertyAnimation, Qt, QTimer
import json
import webbrowser
from pygame import mixer
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import dev

app_version = "1.3.0"
update_description = "Added sound themes, Optimisation of Code, Bug Fix, etc" # Always edit after adding any changes
dev_mode = 0 # 0 - OFF, 1 - ON. Before commits always set 0!

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        self.load_theme() # Load saved theme from app.json
        self.load_sound() # Load saved sound theme from app.json

        self.sound_action = None

        with open ('app.json', 'r') as file:
            data = json.load(file)

        if data.get('sound_enabled') == False:
            self.sound_status = "Enable"
        if data.get('sound_enabled') == True:
            self.sound_status = "Disable"

        with open('app.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.setWindowTitle(f"Splash {app_version}")
        self.setGeometry(100, 100, 405, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(0)

        self.custom_menu_bar = QMenuBar(self)
        self.setMenuBar(self.custom_menu_bar)

        self.main_menu = self.custom_menu_bar.addMenu("Main")
        self.window_menu = self.custom_menu_bar.addMenu("Window")
        self.settings_menu = self.custom_menu_bar.addMenu("Settings")
        self.contribute_menu = self.custom_menu_bar.addMenu("Contribute")
        self.help_menu = self.custom_menu_bar.addMenu("Help")
        self.theme_menu = self.custom_menu_bar.addMenu("Theme")
        self.exit_menu = self.custom_menu_bar.addMenu("Exit")
        
        if dev_mode == 1: self.dev_menu = self.custom_menu_bar.addMenu("DEV") # This menu will be visible only if you turn on a dev mode. You can do it in the beggining of this code

        font = self.custom_menu_bar.font()
        font.setPointSize(8)
        self.custom_menu_bar.setFont(font)

        self.add_action(self.main_menu, "Go to the main menu", self.go_main_menu)
        self.add_action(self.window_menu, "Minimize", self.minimize_window)
        self.add_action(self.window_menu, "Maximize", self.maximize_window)

        self.add_action(self.theme_menu, "Change theme to white", self.change_theme_white)
        self.add_action(self.theme_menu, "Change theme to black", self.change_theme_black)
        self.add_action(self.theme_menu, "Change theme to lime", self.change_theme_lime)
        self.add_action(self.theme_menu, "Change theme to pink", self.change_theme_pink)
        self.add_action(self.theme_menu, "Change theme to purple", self.change_theme_purple)

        self.sound_action = self.add_action(self.settings_menu, f"{self.sound_status} Sound", self.sound_change)
        self.add_action(self.settings_menu, "Change sound theme to Purity", self.set_sound_purity) #FIX
        self.add_action(self.settings_menu, "Change sound theme to Sytrus", self.set_sound_sytrus) #FIX

        self.add_action(self.help_menu, "About", self.about_project)
        self.add_action(self.contribute_menu, "GitHub", self.open_github)
        self.add_action(self.help_menu, "Help", self.open_help)
        self.add_action(self.help_menu, "Documentation", self.open_documentation)
        self.add_action(self.exit_menu, "Exit (Are you sure?)", self.exit_app)

        if dev_mode == 1: self.add_action(self.dev_menu, "DEV",  dev.d_menu)

        self.widget = QLabel()
        pixmap = QPixmap("Splash_Logo_S.png")
        scaled_pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.widget.setPixmap(scaled_pixmap)
        self.widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.main_layout.addWidget(self.widget)

        self.fade(self.widget)
        self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.widget)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Paste URL of video/audio/image (https://www.website.com/...)")
        self.main_layout.addWidget(self.line_edit)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.setFixedSize(200, 25)
        self.ok_button.clicked.connect(self.save_link)
        self.main_layout.addWidget(self.ok_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.thumbnail_file = None
        
        self.button_layout = QHBoxLayout()

        with open ('app.json', 'r') as file:
            data = json.load(file)

        if data.get('update_installed'): # Notificate user about installed updated. Shows once!
            QMessageBox.information(self, "New Update!", f"New Update installed! Current version is {app_version}. We added: {update_description}.")
            data['update_installed'] = False

        with open('app.json', 'w') as file:
             json.dump(data, file, indent=4)

        self.check_updates()

        self.timer = QTimer()
        self.timer.timeout.connect(self.check_sound_status)
        self.timer.start(1000)

    def set_sound_purity(self):
        QMessageBox.information(self, "Sound Theme Changed", "Sound theme is changed to Purity")

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['downloaded_sound'] = "./downloaded_purity.mp3"

        with open('app.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.load_sound()

    def set_sound_sytrus(self):
        QMessageBox.information(self, "Sound Theme Changed", "Sound theme is changed to Sytrus")

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['downloaded_sound'] = "./downloaded_sytrus.mp3"

        with open('app.json', 'w') as file:
            json.dump(data, file, indent=4)

        self.load_sound()

    def sound_check(self):
        with open ('app.json', 'r') as file:
            data = json.load(file)

        if data.get('sound_setting') == "Disable":
            data['sound_setting'] = "Enable"
            self.sound_status = "Enable"
        if data.get('sound_setting') == "Enable":
            data['sound_setting'] = "Disable"
            self.sound_status = "Disable"

        with open('app.json', 'w') as file:
            json.dump(data, file, indent=4)

    def update_sound_action_text(self):
        if self.sound_action:
            self.sound_action.setText(f"{self.sound_status} Sound")
        else:
            print("sound_action is None!")

    def check_sound_status(self):
        with open('app.json', 'r') as file:
            data = json.load(file)

        if data.get('sound_enabled') == False:
            self.sound_status = "Enable"
        else:
            self.sound_status = "Disable"

        self.update_sound_action_text()

    def play_downloaded_sound(self): # Play sound of downloaded file
        with open ('app.json', 'r') as fl:
            sound_setting = json.load(fl)

        if sound_setting.get('sound_enabled'):
            mixer.music.play()
        else:
            print("Sound disabled")

    def load_sound(self): # Load sound theme
        mixer.init()
        with open('app.json', 'r') as file:
            data = json.load(file)

        sound_file = data.get('downloaded_sound')
        if sound_file:
            try:
                mixer.music.load(sound_file) #(sound_file)
                print(f"Using 'downloaded' notification sound: {sound_file}")
            except Exception as e:
                print(f"Error loading sound: {e}")
        else:
            print("Sound not found, error. Please, try to solve this problem and set a sound, because it can cause errors and the app will be closed!")

    def sound_change(self, sound_status): # Change sound setting (turn on-off)
        with open ('app.json', 'r') as file:
            data = json.load(file)

        if data.get('sound_enabled'):
            data['sound_enabled'] = False
            data['sound_setting'] = "Enable"
            QMessageBox.information(self,"Sound disabled", f"Sound disabled. You will not hear any sounds from this applicaton")
            self.sound_status = "Enable"
        else:
            data['sound_enabled'] = True
            data['sound_setting'] = "Disable"
            QMessageBox.information(self,"Sound enabled", f"Sound enabled. You will hear sounds from this applicaton")
            self.sound_status = "Disable"

        with open('app.json', 'w') as file:
            json.dump(data, file, indent=4)

        print(self.sound_status)

    def fade(self, widget): # Small animation
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(3000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def check_updates(self):
        url_fetch = 'https://raw.githubusercontent.com/Vadkon07/VideoXYZ/refs/heads/master/ver.html'
        current_version = app_version

        lines_with_word = self.fetch_lines_with_word(url_fetch, current_version)

        if not lines_with_word:
            self.new_update_notif()

    def fetch_lines_with_word(self, url_fetch, word_fetch):
        response = requests.get(url_fetch)
        soup = BeautifulSoup(response.text, 'html.parser')
        lines = soup.prettify().split('\n')
        filtered_lines = [line for line in lines if word_fetch in line]
        return filtered_lines

    def new_update_notif(self): # If update is found, this window will be shown to user
        dialog = QDialog(self)
        dialog.setWindowTitle("Update Found")

        # Create a QTextBrowser for displaying the HTML content
        text_browser = QTextBrowser(dialog)
        text_browser.setOpenExternalLinks(True)
        text_browser.setHtml(f'<p>New update was found! Do you want to update this app (git should be installed)? Or you can do it manually by visiting our <a href="https://github.com/Vadkon07/Splash">GitHub page</a></p>')

        update_button = QPushButton("Update", dialog)
        update_button.clicked.connect(self.update_from_git)

        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.accept)

        layout = QGridLayout(dialog)
        layout.addWidget(text_browser)
        layout.addWidget(update_button)
        layout.addWidget(close_button)

        dialog.setLayout(layout)
        dialog.exec()

    def add_action(self, menu, name, slot): # It will make creation of QAction easier and faster
        action = QAction(name, self)
        action.triggered.connect(slot)
        menu.addAction(action)
        return action

    def update_from_git(self): # Clone repository from GitHub. This code can be optimised with argv to make it more flexible and universal
        try:
            repo_url = "https://github.com/Vadkon07/Splash"

            subprocess.run(["git", "clone", repo_url], check=True)
            QMessageBox.information(self, "Update Installed", "Repository cloned successfully! You can find her in a folder where you runned this code. You can move her to another place.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}. At first check is git installed on your computer or not. If yes, probably you have some issues with internet connection.")

    def minimize_window(self):
        self.showMinimized()

    def maximize_window(self):
        self.showMaximized()

    def about_project(self):
        QMessageBox.information(self, "About", "Best portable app to download your favorite media content from literally any popular social media! You can download content (from YouTube, X, Soundcloud etc) in literally any popular video/audio format. This application is Open Source, you can find her code on GitHub, or also support developers with donations! You can also download playlists! Notice that if you downloaded a single video, you will also find her thumbnail in a folder where you ran our application.")

    def open_github(self): # Open our GitHub repository in browser
        github_link = "https://github.com/Vadkon07/Splash"

        dialog = QDialog(self)
        dialog.setWindowTitle("Contribute")

        # Create a QTextBrowser for displaying the HTML content
        text_browser = QTextBrowser(dialog)
        text_browser.setOpenExternalLinks(True)  # Allow opening links in the browser
        text_browser.setHtml(f'<p>Visit our <a href="{github_link}">GitHub page</a> for more information.</p>')

        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.accept)

        layout = QGridLayout(dialog)
        layout.addWidget(text_browser)
        layout.addWidget(close_button)

        dialog.setLayout(layout)
        dialog.exec()

    def open_help(self):
        webbrowser.open('https://github.com/Vadkon07/Splash/issues')

    def open_documentation(self):
        webbrowser.open('https://github.com/Vadkon07/Splash/blob/master/README.MD')

    def go_main_menu(self): # Go back to the main menu. It will literally restart app, so it's useful if something goes wrong
        QApplication.closeAllWindows()

        self.window_main = LinkSaver()
        self.window_main.show()

    def change_theme_black(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_black)

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['theme_default'] = "black"

        with open('app.json', 'w') as file:
             json.dump(data, file, indent=4)

    def change_theme_white(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_white)

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['theme_default'] = "white"

        with open('app.json', 'w') as file:
             json.dump(data, file, indent=4)

    def change_theme_lime(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_lime)

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['theme_default'] = "lime"

        with open ('app.json', 'w') as file:
            json.dump(data, file, indent=4)

    def change_theme_pink(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_pink)

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['theme_default'] = "pink"

        with open ('app.json', 'w') as file:
            json.dump(data, file, indent=4)

    def change_theme_purple(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_purple)

        with open ('app.json', 'r') as file:
            data = json.load(file)
            data['theme_default'] = "purple"

        with open ('app.json', 'w') as file:
            json.dump(data, file, indent=4)

    def load_theme(self):
        with open('app.json', 'r') as theme:
            theme_choosed = json.load(theme)

        if theme_choosed.get("theme_default") == "black":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_black)
        if theme_choosed.get("theme_default") == "lime":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_lime)
        if theme_choosed.get("theme_default") == "pink":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_pink)
        if theme_choosed.get("theme_default") == "purple":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_purple)
        else:
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_white)

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            if total_bytes:
                percent = d['downloaded_bytes'] / total_bytes * 100
                self.progress_bar.setValue(int(percent))
        elif d['status'] == 'finished':
            self.progress_bar.setValue(100)

    def exit_app(self):
        sys.exit()

    def save_link(self, title):
        link = self.line_edit.text()
    
        if link:
            self.saved_link = link
            QMessageBox.information(self, "Link Saved", f"Link saved: {link}. Now you have to wait some time...")
        
            try:
                with yt_dlp.YoutubeDL({'quiet': False}) as ydl:
                    info_dict = ydl.extract_info(link, download=False)
                    title = info_dict.get('title', 'Unknown Title')
                
                # Download thumbnail
                    ydl_opts = {
                        'skip_download': True,
                        'writethumbnail': True,
                        'outtmpl': 'thumbnail.%(ext)s',
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl_thumb:
                        info_dict_thumb = ydl_thumb.extract_info(link, download=True)
                        thumbnail_url = info_dict_thumb.get('thumbnail')
                        title = info_dict_thumb.get('title', 'Unknown Title')

                        if thumbnail_url:
                            ext = thumbnail_url.split('.')[-1]
                            self.thumbnail_path = f"./thumbnail.{ext}"
                            print(f"Thumbnail downloaded to: {self.thumbnail_path}")
                            QMessageBox.information(self, "Content found", f"\nContent which we found: {title}")
                        else:
                            QMessageBox.information(self, "Content found", f"\nContent which we found: {title}")
                            self.print_error("Failed to retrieve thumbnail URL (Note that it's normal for playlists, it's not an error)")
                            
            except Exception as e:
                self.print_error(f"Failed to retrieve information. Error description: {e}. Check your intetnet connection and be sure that you entered a valid link.")
                return
                               
            self.show_buttons(link, title)
        else:
            QMessageBox.warning(self, "No Link", "Please paste a link before clicking OK.")

    def show_buttons(self, link, title):
        self.widget.hide()
        self.line_edit.hide()
        self.ok_button.hide()

        self.button_layout = QHBoxLayout()

        self.label = QLabel()
        pixmap = QPixmap('thumbnail.webp')

        pixmap = pixmap.scaled(150, 150, Qt.AspectRatioMode.KeepAspectRatio)
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.label)
        self.setLayout(self.main_layout)

        self.widgetF = QLabel("Choose a format:")
        widget_font = self.widget.font()
        widget_font.setPointSize(12)
        self.widgetF.setFont(widget_font)
        self.widgetF.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.widgetF)

        self.button1 = QPushButton("MP3 (Best only)", self)
        self.button2 = QPushButton("MP4", self)
        self.button3 = QPushButton("Both MP3 + MP4", self)
        self.button4 = QPushButton("WEBM", self)

        self.button1.setFixedSize(100,25)
        self.button2.setFixedSize(100,25)
        self.button3.setFixedSize(100,25)
        self.button4.setFixedSize(100,25)

        self.button_layout.addWidget(self.button1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.button2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.button3, alignment=Qt.AlignmentFlag.AlignCenter)
        self.button_layout.addWidget(self.button4, alignment=Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addLayout(self.button_layout)

        quality_format = None

        self.button1.clicked.connect(lambda: self.choosed_mp3(link, title))
        self.button2.clicked.connect(lambda: self.choose_quality(link))
        self.button3.clicked.connect(lambda: self.choosed_both(link, quality_format, title))
        self.button4.clicked.connect(lambda: self.choosed_webm(link))

    def choose_quality(self, link):
        self.quality_layout = QHBoxLayout()

        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.button4.hide()
        self.widgetF.hide()

        self.widgetQ = QLabel("Choose a quality of video:")
        widget_font = self.widgetQ.font()
        widget_font.setPointSize(12)
        self.widgetQ.setFont(widget_font)
        self.widgetQ.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.widgetQ)

        self.button1 = QPushButton("Worst", self)
        self.button2 = QPushButton("480p", self)
        self.button3 = QPushButton("720p", self)
        self.button4 = QPushButton("Best", self)

        self.button1.clicked.connect(lambda: self.choosed_worst(link))
        self.button2.clicked.connect(lambda: self.choosed_480(link))
        self.button3.clicked.connect(lambda: self.choosed_720(link))
        self.button4.clicked.connect(lambda: self.choosed_best(link))

        self.quality_layout.addWidget(self.button1)
        self.quality_layout.addWidget(self.button2)
        self.quality_layout.addWidget(self.button3)
        self.quality_layout.addWidget(self.button4)

        self.main_layout.addLayout(self.quality_layout)

    def choosed_worst(self, link):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 340, 30)
        self.progress_bar.setMaximum(100)

        self.main_layout.addWidget(self.progress_bar)

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'worstvideo+worstaudio'
        self.choosed_mp4(quality_format, link)

        self.progress_bar.hide()

    def choosed_480(self, link):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 340, 30)
        self.progress_bar.setMaximum(100)

        self.main_layout.addWidget(self.progress_bar)

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'bestvideo[height<=480]+bestaudio'
        self.choosed_mp4(quality_format, link)

        self.progress_bar.hide()

    def choosed_720(self, link):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 340, 30)
        self.progress_bar.setMaximum(100)

        self.main_layout.addWidget(self.progress_bar)

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'bestvideo[height<=720]+bestaudio'
        self.choosed_mp4(quality_format, link)

        self.progress_bar.hide()

    def choosed_best(self, link):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 340, 30)
        self.progress_bar.setMaximum(100)

        self.main_layout.addWidget(self.progress_bar)

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'bestvideo+bestaudio'
        self.choosed_mp4(quality_format, link)

        self.progress_bar.hide()

    def choosed_mp3(self, link, title):
        ydl_opts = {
            'progress_hooks': [self.progress_hook],
            'format': 'bestaudio',
            'outtmpl': os.path.join('MP3', '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
        }

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 340, 30)
        self.progress_bar.setMaximum(100)

        self.main_layout.addWidget(self.progress_bar)

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                ydl.download([link])
                
                self.widget = QLabel(f"Downloaded {title} in MP3 format!")
                self.play_downloaded_sound()
                font = self.widget.font()
                font.setPointSize(12)
                self.widget.setFont(font)
                self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) 
                self.main_layout.addWidget(self.widget)

        except Exception as e:
            self.print_error(f"Failed to download the video: {e}")

        self.progress_bar.hide()

    def choosed_mp4(self, quality_format, link):
        ydl_opts = {
        'progress_hooks': [self.progress_hook],
        'format': quality_format,
        'outtmpl': os.path.join('MP4', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
            }],
        'quiet': False,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                print(f"Video downloaded in {quality_format} format!")
                self.play_downloaded_sound()
                QMessageBox.information(self, "File downloaded", f"File downloaded in {quality_format} format!")
        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.warning(self, "Download failed", f"Failed to download file: {e}")


    def choosed_both(self, link, quality_format, title):
        self.choose_quality(link)
        self.choosed_mp4(quality_format, link)
        self.choosed_mp3(link, title)

    def choosed_webm(self, link):
        ydl_opts = {
        'progress_hooks': [self.progress_hook],
        'format': 'bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]/best',
        'outtmpl': os.path.join('WEBM', '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'webm',
            }],
        'quiet': False,
        }

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(30, 40, 340, 30)
        self.progress_bar.setMaximum(100)

        self.main_layout.addWidget(self.progress_bar)

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")


        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                print(f"Video downloaded in best quality!")
                self.play_downloaded_sound()
                QMessageBox.information(self, "File downloaded", f"File downloaded in best quality!")
        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.warning(self, "Download failed", f"Failed to download file: {e}")

        self.progress_bar.hide()

        self.show_buttons(link)


    def print_error(self, message):
        print(f"Error message: {message}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    custom_stylesheet_black = """
    QWidget {
        background-color: #1a1a1a;
        color: white;
    }
    QMenuBar {
        background-color: #1a1a1a;
        color: white;
    }
    QMenuBar::item {
        background-color: #1a1a1a;
    }
    QMenuBar::item:selected {
        background: #697565;
        color: white;
    }
    QPushButton {
        background-color: #97fff5;
        color: black;
    }
    QPushButton:hover {
        background-color: #cc0000;
    }
    QMenu {
        background-color: #3C3D37;
        color: white;
    }
    QMenu::item {
        background-color: #3C3D37;
        color: white;
    }
    QProgressBar {
        border: 2px solid grey;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: red;
    }
   """

    custom_stylesheet_white = """
    QWidget {
        background-color: white;
        color: black;
    }
    QMenuBar {
        background-color: white;
        color: black;
    }
    QMenuBar::item {
        background-color: white;
        color: black;
    }
    QMenuBar::item:selected {
        background: grey;
        color: white;
    }
    QLineEdit {
        background-color: white;
        color: black;
    }
    QLine {
        color: grey;
    }
    QPushButton {
        background-color: #97fff5;
        color: black;
    }
    QPushButton:hover {
        background-color: #cc0000;
    }
    QMenu {
        background-color: #1a1a1a;
        color: white;
    }
    QMenu::item {
        background-color: grey;
        color: white;
    }
    QProgressBar {
        border: 2px solid grey;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: red;
    }
   """

    custom_stylesheet_lime = """
    QWidget {
        background-color: lime;
        color: black;
    }
    QMenuBar {
        background-color: lime;
        color: black;
    }
    QMenuBar::item {
        background-color: lime;
        color: black;
    }
    QMenuBar::item:selected {
        background: grey;
        color: white;
    }
    QLineEdit {
        background-color: lime;
        color: black;
    }
    QLine {
        color: grey;
    }
    QPushButton {
        background-color: #97fff5;
        color: black;
    }
    QPushButton:hover {
        background-color: #cc0000;
    }
    QMenu {
        background-color: #1a1a1a;
        color: black;
    }
    QMenu::item {
        background-color: lime;
        color: black;
    }
    QProgressBar {
        border: 2px solid grey;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: red;
    }
    """

    custom_stylesheet_pink = """
    QWidget {
        background-color: pink;
        color: black;
    }
    QMenuBar {
        background-color: pink;
        color: black;
    }
    QMenuBar::item {
        background-color: pink;
        color: black;
    }
    QMenuBar::item:selected {
        background: pink;
        color: black;
    }
    QLineEdit {
        background-color: pink;
        color: black;
    }
    QLine {
        color: grey;
    }
    QPushButton {
        background-color: #97fff5;
        color: black;
    }
    QPushButton:hover {
        background-color: #cc0000;
    }
    QMenu {
        background-color: #1a1a1a;
        color: black;
    }
    QMenu::item {
        background-color: grey;
        color: black;
    }
    QProgressBar {
        border: 2px solid grey;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: red;
    }
    """

    custom_stylesheet_purple = """
    QWidget {
        background-color: purple;
        color: white;
    }
    QMenuBar {
        background-color: purple;
        color: white;
    }
    QMenuBar::item {
        background-color: purple;
        color: white;
    }
    QMenuBar::item:selected {
        background: grey;
        color: white;
    }
    QLineEdit {
        background-color: purple;
        color: white;
    }
    QLine {
        color: grey;
    }
    QPushButton {
        background-color: #97fff5;
        color: black;
    }
    QPushButton:hover {
        background-color: #cc0000;
    }
    QMenu {
        background-color: #1a1a1a;
        color: white;
    }
    QMenu::item {
        background-color: grey;
        color: white;
    }
    QProgressBar {
        border: 2px solid grey;
        text-align: center;
    }
    QProgressBar::chunk {
        background-color: red;
    }
    """

    window = MainMenu()
    window.show()
    sys.exit(app.exec())
