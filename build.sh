#!/bin/bash
pyinstaller --onefile --hidden-import win10toast --hidden-import PyQt5 --name time-care --icon=break.ico --add-data "break.png;." --noconsole main.py