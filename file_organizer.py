

# simple file organizer
# Before running, make sure that you already created folders named after your extensions.

import os  # to access files and directories
import shutil # for file movements

# With expanduser, you do not need to define the path.
# Jut include whatever folder you want to organize, and it'll do the work for you. 
directory = os.path.join(os.path.expanduser("~"), "Desktop") 

# list of extensions
extensions = {
    ".jpg": "images",
    ".png": "images",
    ".gif": "images",
    ".mp4": "videos",
    ".mkv": "videos",
    ".docx": "documents",
    ".doc": "documents",
    ".pdf": "documents",
    ".txt": "documents",
    ".csv": "documents",
    ".mp3": "music",
    ".wav": "music"
    
}
# scans for the lists of your files in the directory.
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path): # just to check if it is a file. 
        extension = os.path.splitext(filename)[1].lower() # split the text and making everything lowercase
        
        if extension in extensions: # check if files are on the list of extensions.
            folder_name = extensions[extension]
            
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok = True)
            
            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)
            
            print(f"Moved {filename} to {folder_name} folder.")
            
        else:
            print(f"Skipped {filename}. Unknown file extension. ")
    else:
        print(f"Skipped {filename}. It is a directory.")
        
print("File Organization Complete!")