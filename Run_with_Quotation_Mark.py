import os

path = input("Please Enter the Path of The File or Drag and Drop the File Inside The Terminal : ")

# Get the absolute path of the file
abs_path = os.path.abspath(path)

# Check if the path is valid
#if os.path.exists(abs_path):
    # Run the script
#    os.system('python ReleaseInfoCreator.py ' + abs_path)
#else:
    # Print an error message
#    print("Error: Invalid Path")

# Check if the path contains spaces
if '' in path:
    # Replace the spaces with '\ '
    abs_path = abs_path.replace('"', '')
    # Run the script
    os.system('python ReleaseInfoCreator.py ' + abs_path)
    os.system('python TorrentCreator.py ' + abs_path)

    # Wait for user input before exiting
    input("Press Enter to exit...")