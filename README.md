Thuneder-Upload Version 3.001

[Read What's New](https://raw.githubusercontent.com/ItzMeBeluga/Thunder-Upload/main/what's-new.txt)


## Important:

1. Install python 3.10.7 (or any version from 3.8.x to 3.10.x), be sure to add python to PATH while installing it

https://www.python.org/ftp/python/3.10.7/python-3.10.7-amd64.exe

https://datatofish.com/add-python-to-windows-path/

## Setup:

1. Run the ```Install requirements.bat``` or run this command on terminal ``` pip install -r requirements.txt ```

2. Edit the ```RelaseInfoCreator.json``` and set image host api_key (imgbb recomemded)

3. Go to https://api.imgbb.com/ and get your api key.

4. For Fastest use create a shortcut of ```Thuneder-Upload.exe``` and move it to desktop.

##  How to Use:

1. Run ```Thuneder-Upload.exe``` and it will open a console window 
    drag and drop your media file to the terminal.

    It will genarate Mediainfo + Screenshots and will upload them for you to your selected image host + it will create a .torrent of the file 

## note:

There shouldn't be any space in the name of the file or it may show some error. 

## Torrent Creator Section

## Usage:
```
python TorrentCreator.py -p : Show current path for .torrent file output and announce URL.

python TorrentCreator.py -np : Set a new path for .torrent file output.

python TorrentCreator.py -a : Show current announce URL.

python TorrentCreator.py -na : Set a new announce URL.
