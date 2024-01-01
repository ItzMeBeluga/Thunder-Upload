# Thunder Upload - Simplifying Torrent Uploads

## Introduction

**Happy New Year 2024!**

Welcome to **Thunder Upload**, a user-friendly tool designed to streamline the process of uploading torrents for Windows PC users. This tool automates the creation of MediaInfo for your files, captures screenshots of your video files, uploads them to IMGBB, and generates the .torrent meta-file—all with just a few clicks.

## Features

- **MediaInfo Creation:** Automatically generates detailed information about your file.
- **Screenshot Capture:** Takes screenshots of your video file for preview.
- **IMGBB Integration:** Uploads screenshots to IMGBB for easy sharing.
- **.torrent Meta-file Generation:** Creates the necessary .torrent file for your video.

## Installation Guide

### 1. Install Python

- Download [Python 3.9.13](https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe) and install it.
- During installation, ensure to **Add Python to Environment Variables**.
- Confirm the installation by running `python --version` in the command prompt.

### 2. Download and Setup the Tool

1. Visit the [GitHub repository](https://github.com/ItzMeBeluga/Thunder-Upload) and download the zip file.
2. Unzip the file and navigate to the Thunder-Upload folder.
3. Open the command prompt in the folder and run `pip install -r requirements.txt` or use `Install requirements.bat`.
4. Edit the `RelaseInfoCreator.json` file and set the image host API key (IMGBB recommended).
5. Obtain your IMGBB API key from [https://api.imgbb.com/](https://api.imgbb.com/).
6. Run `Change & Add Announce URL.bat` to set the announce URL.
7. Run `Change .torrent Output Path.bat` to set the path for exporting .torrent files.

## Usage Guide

### .BAT Method

1. Double click on `Thunder-Upload.bat` to open the terminal.
2. Drag and drop your video file into the terminal, press enter, and wait for the processes to complete.
3. After completion, the terminal will display URLs for MediaInfo, screenshot, and the location of the exported .torrent file.

**Note:** For now, only one video file at a time is compatible with this script. Folder support will be added in the future. Additionally, files with spaces in their names may encounter issues, but this will be addressed in future updates.

## Executable Conversion

To convert `Thunder-Upload.bat` to an executable file for convenience, use the `Advance_Bat_To_EXE.exe` in the `bin` folder. Refer to [this video](https://www.awesomescreenshot.com/video/23667393?key=d2858db8447766a4283fa40b4a5847df) for a guide on creating an executable file.

**Note:** This tool is currently available for Windows users only. Regular updates will be provided to enhance its functionality.

Feel free to contribute, report issues, or suggest improvements on the [GitHub page](https://github.com/ItzMeBeluga/Thunder-Upload). Happy sharing!

## Credits
Thanks to [BC44](https://github.com/BC44) for the [Release Info Creator](https://github.com/BC44/Release-Info-Creator) script.
