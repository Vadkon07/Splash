import sys
import os
import subprocess
import qdarkstyle
import markdown
import yt_dlp
import time
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout, QMainWindow, QMenuBar, QTextBrowser, QDialog, QGridLayout, QLabel, QScrollArea, QGraphicsOpacityEffect
from PyQt6.QtGui import QAction, QImage, QPixmap
from PyQt6.QtCore import QPropertyAnimation, Qt
import json


class ImageWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.setWindowTitle("Thumbnail Viewer")
        layout = QVBoxLayout()
        self.label = QLabel()
        pixmap = QPixmap('maxresdefault [maxresdefault].webp') #or jpg, we have to solve it
        self.label.setPixmap(pixmap)
        layout.addWidget(self.label)
        self.setLayout(layout)

class LinkSaver(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Downloader")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setSpacing(0)

        self.custom_menu_bar = QMenuBar(self)
        self.setMenuBar(self.custom_menu_bar)

        self.main_menu = self.custom_menu_bar.addMenu("Main")
        self.window_menu = self.custom_menu_bar.addMenu("Window")
        self.settings_menu = self.custom_menu_bar.addMenu("Settings")
        self.version_menu = self.custom_menu_bar.addMenu("Version")
        self.contribute_menu = self.custom_menu_bar.addMenu("Contribute")
        self.help_menu = self.custom_menu_bar.addMenu("Help")
        self.exit_menu = self.custom_menu_bar.addMenu("Exit")


        self.add_action(self.main_menu, "Main", self.window) #doesn't work, not finished
        self.add_action(self.window_menu, "Minimize", self.minimize_window)
        self.add_action(self.window_menu, "Maximize", self.maximize_window)
        self.add_action(self.settings_menu, "Preferences", self.open_preferences)
        self.add_action(self.version_menu, "About", self.show_version)
        self.add_action(self.contribute_menu, "GitHub", self.open_github)
        self.add_action(self.help_menu, "Documentation", self.open_documentation)
        self.add_action(self.exit_menu, "Exit (Are you sure?)", self.exit_app)

        self.widget = QLabel("YouTube Downloader")
        self.fade(self.widget)
        font = self.widget.font()
        font.setPointSize(18)
        self.widget.setFont(font)
        self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) 
        self.main_layout.addWidget(self.widget)

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Paste URL of YouTube video here")
        self.line_edit.setStyleSheet("QLineEdit { color: white; }")
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
            QMessageBox.information(self, "New Update!", f"New Update installed! Current version is v0.01. Click 'Ok' to hide this message forever")
            data['update_installed'] = False

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

    def show_version(self):
        QMessageBox.information(self, "Version", "YouTube Downloader v0.1")

    def open_github(self):
        # Define the GitHub link
        github_link = "https://github.com/your-repository"  # Replace with your actual GitHub link

        # Create a custom dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Contribute")

        # Create a QTextBrowser for displaying the HTML content
        text_browser = QTextBrowser(dialog)
        text_browser.setOpenExternalLinks(True)  # Allow opening links in the browser
        text_browser.setHtml(f'<p>Visit our <a href="{github_link}">GitHub page</a> for more information.</p>')

        # Add a close button
        close_button = QPushButton("Close", dialog)
        close_button.clicked.connect(dialog.accept)  # Only closes the dialog

        # Layout setup
        layout = QGridLayout(dialog)
        layout.addWidget(text_browser)
        layout.addWidget(close_button)

        dialog.setLayout(layout)
        dialog.exec()

    def open_documentation(self):
        dialog = DocumentationDialog()
        dialog.exec()

    def exit_app(self):
        sys.exit()

        # Convert Markdown to HTML
        html_text = markdown.markdown(markdown_text)

        # Create a custom dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Help Documentation")
        dialog.setFixedSize(600, 400)  # Adjust the size as needed

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
            print(link)
        
            try:
                with yt_dlp.YoutubeDL({'quiet': False}) as ydl:
                    info_dict = ydl.extract_info(link, download=False)
                    title = info_dict.get('title', None)
                
                # Download thumbnail
                    ydl_opts = {
                        'skip_download': True,
                        'write_thumbnail': True,
                        'outtmpl': '%(title)s.%(ext)s',
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl_thumb:
                        info_dict_thumb = ydl_thumb.extract_info(link, download=True)
                        thumbnail_url = info_dict_thumb.get('thumbnail')
                        title = info_dict_thumb.get('title')
                        ext = thumbnail_url.split('.')[-1]
                        self.thumbnail_path = f"{title}.{ext}"
                        print(f"Thumbnail downloaded to: {self.thumbnail_path}") 

                        #ydl.download([link])
            except Exception as e:
                self.print_error(f"Failed to retrieve video information: {e}")
                return
        
            QMessageBox.information(self, "Video found", f"\nVideo found: {title}")
        
            self.show_image_in_messagebox(self.thumbnail_path)
                  
            self.show_buttons(link, title)
        else:
            QMessageBox.warning(self, "No Link", "Please paste a link before clicking OK.")

    def show_buttons(self, link, title):
        self.widget.hide()
        self.line_edit.hide()
        self.ok_button.hide()

        self.button_layout = QHBoxLayout()

        self.button1 = QPushButton("MP3 (Best)", self)
        self.button2 = QPushButton("MP4", self)
        self.button3 = QPushButton("Both", self)

        self.button_layout.addWidget(self.button1)
        self.button_layout.addWidget(self.button2)
        self.button_layout.addWidget(self.button3)

        self.main_layout.addLayout(self.button_layout)

        self.button1.clicked.connect(lambda: self.choosed_mp3(link, title))
        self.button2.clicked.connect(lambda: self.choose_quality(link))
        self.button3.clicked.connect(lambda: self.choosed_both(link))

    def choose_quality(self, link):
        self.quality_layout = QHBoxLayout()

        self.button1.hide()
        self.button2.hide()
        self.button3.hide()

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
        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'worstvideo+worstaudio'
        self.choosed_mp4(quality_format, link)

    def choosed_480(self, link):
        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'bestvideo[height<=480]+bestaudio'
        self.choosed_mp4(quality_format, link)

    def choosed_720(self, link):
        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'bestvideo[height<=720]+bestaudio'
        self.choosed_mp4(quality_format, link)

    def choosed_best(self, link):
        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")
        quality_format = 'bestvideo+bestaudio'
        self.choosed_mp4(quality_format, link)

    def choosed_mp3(self, link, title):

        #self.notif = QLabel("Downloading mp3...")
        #font = self.notif.font()
        #font.setPointSize(18)
        #self.notif.setFont(font)
        #self.notif.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) 
        #self.main_layout.addWidget(self.notif)

        #time.sleep(2)

        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': os.path.join('%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
        }

        QMessageBox.information(self, "Downloading...", f"We started to download your file, now you have to wait some time. We will notificate you when we will download this file.")

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:

                ydl.download([link])
                
                self.widget = QLabel(f"Downloaded {title} in MP3 format!")
                font = self.widget.font()
                font.setPointSize(12)
                self.widget.setFont(font)
                self.widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter) 
                self.main_layout.addWidget(self.widget)

        except Exception as e:
            self.print_error(f"Failed to download the video: {e}")

    def choosed_mp4(self, quality_format, link):
        ydl_opts = {
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
                QMessageBox.information(self, "File downloaded", f"File downloaded in {quality_format} format!")
        except Exception as e:
            print(f"Error: {e}")
            QMessageBox.warning(self, "Download failed", f"Failed to download file: {e}")

    def choosed_both(self, link):
        print("TEST BOTH")

    def print_error(self, message):
        print(f"Error message: {message}")


class DocumentationDialog(QDialog):
      def __init__(self):
        super().__init__()
        self.setWindowTitle("Documentation")
        self.resize(640, 480)  # Set initial size

        # Create a QVBoxLayout
        layout = QVBoxLayout()

        # Create a QLabel with Markdown content
        label = QLabel("""
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

        ## License

        This project is licensed under the [MIT License](./LICENSE).

        """)

        label.setTextFormat(Qt.TextFormat.MarkdownText)
        label.setWordWrap(True)

        # Create a QScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(label)

        # Add the QScrollArea to the layout
        layout.addWidget(scroll_area)

        # Add a close button
        button_layout = QHBoxLayout()
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        layout.addLayout(button_layout)

        # Set the layout for the dialog
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    custom_stylesheet = """
    QWidget {
        background-color: #1a1a1a;  /* Very dark background */
    }
    QPushButton {
        background-color: #ff0000;  /* Red buttons */
        color: white;  /* Text color */
    }
    QPushButton:hover {
        background-color: #cc0000;  /* Darker red on hover */
    }
   """
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6() + custom_stylesheet)
    window = LinkSaver()
    window.show()
    sys.exit(app.exec())
