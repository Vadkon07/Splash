import yt_dlp
import os
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QHBoxLayout

from darktheme.widget_template_pyqt6 import DarkApplication, DarkPalette

print("Running app. Wait some seconds...")

class LinkSaver(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("YouTube Downloade")
        self.setGeometry(100, 100, 300, 100)

        self.layout = QVBoxLayout()

        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Paste URL of YouTube video here")
        self.line_edit.setStyleSheet("QLineEdit { color: white; }")
        self.layout.addWidget(self.line_edit)

        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.save_link)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

    def save_link(self):
        link = self.line_edit.text()

        if link:
            self.saved_link = link
            QMessageBox.information(self, "Link Saved", f"Link saved: {link}. Now you have to wait some time...")
            print(link)

            try:
                with yt_dlp.YoutubeDL({'quiet': False}) as ydl:
                    info_dict = ydl.extract_info(link, download=False)
                    title = info_dict.get('title', None)
                    if not title:
                        raise ValueError("Unable to retrieve video title.")
            except Exception as e:
                print_error(f"Failed to retrieve video information: {e}")
                exit(1)

            print(f"\nVideo found: {title}")

            self.show_buttons(link)
        else:
            QMessageBox.warning(self, "No Link", "Please paste a link before clicking OK.")

    def show_buttons(self, link):
        self.line_edit.hide()
        self.ok_button.hide()

        self.button_layout = QHBoxLayout()

        self.button1 = QPushButton("MP3", self)
        self.button2 = QPushButton("MP4", self)
        self.button3 = QPushButton("Both", self)

        self.button_layout.addWidget(self.button1)
        self.button_layout.addWidget(self.button2)
        self.button_layout.addWidget(self.button3)

        self.layout.addLayout(self.button_layout)

        self.button1.clicked.connect(lambda: self.choosed_mp3(link)) #ERROR: Without this (link) he shows menu with choice of format, but doesn't woerk. But with (link) it works, but also skips choice of format
        self.button2.clicked.connect(lambda: self.choosed_mp4)
        self.button3.clicked.connect(lambda: self.choosed_both)

        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)

        #self.choose_quality()

    def choose_quality(self):
        self.quality_layout = QHBoxLayout()
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()

        self.button1 = QPushButton("Lowest", self)
        self.button2 = QPushButton("480p", self)
        self.button3 = QPushButton("720p", self)
        self.button4 = QPushButton("Highest", self)

        self.quality_layout.addWidget(self.button1)
        self.quality_layout.addWidget(self.button2)
        self.quality_layout.addWidget(self.button3)
        self.quality_layout.addWidget(self.button4)


        self.layout.addLayout(self.quality_layout)

    def choosed_mp3(self, link):
        ydl_opts = {
                'format': 'bestaudio',
                # here add path to output ---
                'outtmpl': os.path.join('%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'quiet': False,
                }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
                print(f"{title} downloaded!")
        except Exception as e:
            print_error(f"Failed to download the video: {e}")
            exit(1)

    def choosed_mp4(self):
        print("TEST MP4")

    def choosed_both(self):
        print("TEST BOTH")


def print_error(message):
    print(f"Error message: {message}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setPalette(DarkPalette())
    window = LinkSaver()
    window.show()
    sys.exit(app.exec())

