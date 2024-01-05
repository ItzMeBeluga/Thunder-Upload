@echo off
set /p "inputPath=Please Enter the Path of The File or Drag and Drop the File Inside The Terminal : "
python ReleaseInfoCreator.py %inputPath%
pause
