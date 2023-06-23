import sys
import ctypes
import datetime
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QColor, QPalette, QIcon
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QDialog,
    QTextEdit,
    QMessageBox,
)
from win11toast import toast

FONT_SIZE_14="font-size: 14px;"
class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("break.png")) 
        self.setWindowTitle("About")
        self.setFixedSize(200, 100)
        self.setStyleSheet("background-color: #333333; color: white;")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(5)
        
        #version
        version_label = QLabel("Version: 1.0", self)
        version_label.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(version_label)
        #author
        author_label = QLabel("Author: Nipu Chakraborty", self)
        author_label.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(author_label)

        #email
        author_email = QLabel("Email: pro.nipu@gmail.com", self)
        author_email.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(author_email)

class TimerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Timer")
        self.setWindowIcon(QIcon("break.png")) 
        self.setGeometry(100, 100, 250, 200)
        self.setStyleSheet("background-color: #333333; color: white;")

        # Create a central widget and a layout for it
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(10)

        self.timer_label = QLabel(self)
        self.timer_label.setText("00:00:00")
        self.timer_label.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.timer_label)

        self.current_time_label = QLabel(self)
        self.current_time_label.setText("Current Time")
        self.current_time_label.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.current_time_label)

        self.duration_label = QLabel("Duration (minutes):", self)
        self.duration_label.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.duration_label)

        self.duration_input = QLineEdit(self)
        self.duration_input.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.duration_input)

        self.task_label = QLabel("Task you working on:", self)
        self.task_label.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.task_label)

        self.task_input = QTextEdit(self)
        self.task_input.setText("0")
        self.task_input.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.task_input)

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_timer)
        self.start_button.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.clicked.connect(self.stop_timer)
        self.stop_button.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.stop_button)

        self.about_button = QPushButton("About", self)
        self.about_button.clicked.connect(self.show_about_dialog)
        self.about_button.setStyleSheet(f"{FONT_SIZE_14}")
        layout.addWidget(self.about_button)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.time_elapsed = 0
        self.setCentralWidget(central_widget)

    def update_timer(self):
        self.time_elapsed += 1
        hours = self.time_elapsed // 3600
        minutes = (self.time_elapsed % 3600) // 60
        seconds = self.time_elapsed % 60
        self.timer_label.setText(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        self.current_time_label.setText(f"Current Time: {current_time}")

        duration = int(self.duration_input.text())
        if self.time_elapsed >= duration * 60:
            self.stop_timer()
            toast("Take a break!", "Take care of your back.", duration="long", buttons=["reminder"])
            ctypes.windll.user32.LockWorkStation()
            task = self.task_input.toPlainText()
            print(f"You worked on: {task}")

    def start_timer(self):
         input_value = self.duration_input.text()
         if input_value=="":
            QMessageBox.warning(
                self,
                "Invalid Duration",
                "Please enter a valid positive integer for the duration.",
                QMessageBox.Ok
            )
            return
         duration = int(input_value)
         if duration > 0:
            self.time_elapsed = 0
            self.timer.start(1000)

    def stop_timer(self):
        self.timer.stop()

    def show_about_dialog(self):
        about_dialog = AboutDialog()
        about_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor("#333333"))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor("#333333"))
    dark_palette.setColor(QPalette.AlternateBase, QColor("#444444"))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor("#666666"))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor("#4A90E2"))
    dark_palette.setColor(QPalette.Highlight, QColor("#4A90E2"))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(dark_palette)

    window = TimerWindow()
    window.show()
    sys.exit(app.exec_())