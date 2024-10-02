import sys
import os
import subprocess
import qdarkstyle
import markdown
import yt_dlp
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QMainWindow, QMenuBar, QTextBrowser, QDialog, QGridLayout, QLabel, QScrollArea, QProgressBar, QGraphicsOpacityEffect
from PyQt6.QtGui import QAction, QImage, QPixmap
from PyQt6.QtCore import QPropertyAnimation, Qt
import json
import webbrowser
from pygame import mixer
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET
import dev #for developers only

app_version = "v0.8.0"
update_description = "New GUI, New Feature, Optimised Performance, etc" # Will be added very soon

class ImageWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Thumbnail Viewer")
        layout = QVBoxLayout()
        self.label = QLabel()
        pixmap = QPixmap('thumbnail.webp')
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)

class LinkSaver(QMainWindow):
    def __init__(self):
        super().__init__()

        self.check_updates()

        self.load_theme()

        self.setWindowTitle(f"VideoXYZ {app_version}")
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
        #self.dev_menu = self.custom_menu_bar.addMenu("DEV") #UNCOMMENT TO SHOW DEVELOPER MENU

        self.add_action(self.main_menu, "Go to the main menu", self.go_main_menu)
        self.add_action(self.window_menu, "Minimize", self.minimize_window)
        self.add_action(self.window_menu, "Maximize", self.maximize_window)

        self.add_action(self.theme_menu, "Change theme to white", self.change_theme_white)
        self.add_action(self.theme_menu, "Change theme to black", self.change_theme_black)
        self.add_action(self.theme_menu, "Change theme to lime", self.change_theme_lime)
        self.add_action(self.theme_menu, "Change theme to pink", self.change_theme_pink)
        self.add_action(self.theme_menu, "Change theme to purple", self.change_theme_purple)

        self.add_action(self.settings_menu, "Sound ON/OFF", self.sound_change)
        self.add_action(self.help_menu, "About", self.about_project)
        self.add_action(self.contribute_menu, "GitHub", self.open_github)
        self.add_action(self.help_menu, "Help", self.open_help)
        self.add_action(self.help_menu, "Documentation", self.open_documentation)
        self.add_action(self.exit_menu, "Exit (Are you sure?)", self.exit_app)
        #self.add_action(self.dev_menu, "DEV",  dev.d_menu) #UNCOMMENT TO SHOW DEVELOPER MENU

        self.widget = QLabel(f"VideoXYZ")
        #self.fade(self.widget)
        widget_font = self.widget.font()
        widget_font.setPointSize(18)
        self.widget.setFont(widget_font)
        self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.widget)

        self.ver_widget = QLabel(f"{app_version}")
        self.fade(self.ver_widget)
        ver_font = self.ver_widget.font()
        ver_font.setPointSize(10)
        self.ver_widget.setFont(ver_font)
        self.ver_widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.ver_widget)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Paste URL of YouTube video here (https://www.youtube.com/watch...)")
        self.main_layout.addWidget(self.line_edit)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.setFixedSize(200, 25)
        self.ok_button.clicked.connect(self.save_link)
        self.main_layout.addWidget(self.ok_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.thumbnail_file = None
        
        self.button_layout = QHBoxLayout()

        with open ('app.json', 'r') as file:
            data = json.load(file)

        if data.get('update_installed'):
            QMessageBox.information(self, "New Update!", f"New Update installed! Current version is {app_version}. We added: improved GUI, optimised code, added purple theme") # !!! UPDATE NOTIFICATION !!!
            data['update_installed'] = False

        with open('app.json', 'w') as file:
             json.dump(data, file, indent=4)

        
    def play_downloaded_sound(self):
        with open ('app.json', 'r') as fl:
            sound_setting = json.load(fl)

        if sound_setting.get('sound_enabled'):
            mixer.music.play()
        else:
            print("Sound disabled")

    def sound_change(self):
        with open ('app.json', 'r') as file:
            data = json.load(file)

        if data.get('sound_enabled'):
            data['sound_enabled'] = False
            QMessageBox.information(self,"Sound disabled", f"Sound disabled. You will not hear any sounds from this applicaton")
        else:
            data['sound_enabled'] = True
            QMessageBox.information(self,"Sound enabled", f"Sound enabled. You will hear sounds from this applicaton")

        with open('app.json', 'w') as file:
            json.dump(data, file, indent=4)

    def fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        self.animation = QPropertyAnimation(self.effect, b"opacity")
        self.animation.setDuration(2000)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def check_updates(self):
        url_fetch = 'https://raw.githubusercontent.com/Vadkon07/VideoXYZ/refs/heads/master/ver.html'
        word_fetch = app_version
        #if word_fetch not found, ent

        lines_with_word = self.fetch_lines_with_word(url_fetch, word_fetch)

        for line in lines_with_word:
            highlighted_line = line.replace(word_fetch, f"\033[1;31m{word_fetch}\033[0m")

            print(highlighted_line)

            if highlighted_line == app_version:
                new_update_notif()

    def fetch_lines_with_word(self, url_fetch, word_fetch):
        response = requests.get(url_fetch)
        soup = BeautifulSoup(response.text, 'html.parser')
        lines = soup.prettify().split('\n')
        filtered_lines = [line for line in lines if word_fetch in line]
        return filtered_lines

    def new_update_notif(self):
        print("New Update Found!")

    def add_action(self, menu, name, slot):
        action = QAction(name, self)
        action.triggered.connect(slot)
        menu.addAction(action)

    def minimize_window(self):
        self.showMinimized()

    def maximize_window(self):
        self.showMaximized()

    def open_preferences(self):
        QMessageBox.information(self, "Preferences", "Preferences dialog (not implemented).")

    def about_project(self):
        QMessageBox.information(self, "About", "Best portable app to download your favorite media content from YouTube! You can download YouTube videos in literally any popular video/audio format. This application is Open Source, you can find her code on GitHub, or also support developers with donations! You can also download playlists! Notice that if you downloaded a single video, you will also find her thumbnail in a folder where you ran our application.")

    def open_github(self):

        github_link = "https://github.com/Vadkon07/VideoXYZ"

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
        webbrowser.open('https://github.com/Vadkon07/VideoXYZ/issues')

    def open_documentation(self):
        webbrowser.open('https://github.com/Vadkon07/VideoXYZ/blob/master/README.MD')

    def go_main_menu(self):
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

        if theme_choosed.get("theme_default") == "white":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_white)
        if theme_choosed.get("theme_default") == "lime":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_lime)
        if theme_choosed.get("theme_default") == "pink":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_pink)
        if theme_choosed.get("theme_default") == "purple":
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_purple)
        else:
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet_black)


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

        # Convert Markdown to HTML
        html_text = markdown.markdown(markdown_text)

        # Create a custom dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Help Documentation")
        dialog.setFixedSize(600, 350)  # Adjust the size as needed

        # Create a QTextBrowser for displaying the HTML content
        text_browser = QTextBrowser(dialog)
        text_browser.setHtml(html_text)
        text_browser.setOpenExternalLinks(True)  # Allow opening links in the browser

        # Add a close button
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.accept)  # Close the dialog

        # Layout setup
        layout = QVBoxLayout(dialog)
        layout.addWidget(text_browser)
        layout.addWidget(close_button, alignment=Qt.AlignmentFlag.AlignCenter)  # Center the button horizontally

        layout.setContentsMargins(10, 10, 10, 10)  # Add some margin to the layout for aesthetics
        layout.setSpacing(10)  # Add some spacing between the text and button

        dialog.setLayout(layout)
        dialog.exec()

    def show_image_in_messagebox(self, thumbnail_path):
        self.image_window = ImageWindow(thumbnail_path)
        self.image_window.show()

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
                            QMessageBox.information(self, "Video found", f"\nVideo found: {title}")
                            self.show_image_in_messagebox(self.thumbnail_path)

                        else:
                            QMessageBox.information(self, "Video found", f"\nVideo found: {title}")
                            self.print_error("Failed to retrieve thumbnail URL (Note that it's normal for playlists, it's not an error)")
                            
            except Exception as e:
                self.print_error(f"Failed to retrieve video information. Error description: {e}")
                return
                               
            self.show_buttons(link, title)
        else:
            QMessageBox.warning(self, "No Link", "Please paste a link before clicking OK.")

    def show_buttons(self, link, title):
        self.widget.hide()
        self.ver_widget.hide()
        self.line_edit.hide()
        self.ok_button.hide()

        self.button_layout = QHBoxLayout()

        self.widget = QLabel("Choose a format:")
        widget_font = self.widget.font()
        widget_font.setPointSize(12)
        self.widget.setFont(widget_font)
        self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        self.main_layout.addWidget(self.widget)

        self.button1 = QPushButton("MP3 (Best quality only)", self)
        self.button2 = QPushButton("MP4", self)
        self.button3 = QPushButton("Both MP3 + MP4", self)
        self.button4 = QPushButton("Webm", self)

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
        self.widget.hide()

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
            'outtmpl': os.path.join('%(title)s.%(ext)s'),
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
        'outtmpl': os.path.join('%(title)s.%(ext)s'),
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
        'outtmpl': os.path.join('%(title)s.%(ext)s'),
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

    mixer.init()
    mixer.music.load('./downloaded.mp3')

    custom_stylesheet_black = """
    QWidget {
        background-color: #1a1a1a;  /* Very dark background */
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
        background-color: #ff0000;
        color: white;
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
   #"""

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
        background-color: #ff0000;
        color: white;
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
        background-color: #ff0000;  /* Red buttons */
        color: white;  /* Text color */
    }
    QPushButton:hover {
        background-color: #cc0000;  /* Darker red on hover */
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
        background-color: #ff0000;  /* Red buttons */
        color: white;  /* Text color */
    }
    QPushButton:hover {
        background-color: #cc0000;  /* Darker red on hover */
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
        background-color: #ff0000;
        color: white;
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



    window = LinkSaver()
    window.show()
    sys.exit(app.exec())
