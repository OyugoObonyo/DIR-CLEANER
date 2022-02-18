import os
import shutil
from os import path

extensions = {
    "COMPRESSED": ["tar", "zip", "rar"],
    "DOCUMENTS": ["doc", "docx", "pdf"],
    "MUSIC": ["mp3", "m4A", "flac", "wav", "aac"],
    "PICTURES": ["png", "jpg", "jpeg", "gif", "bmp", "tiff"],
    "VIDEOS": ["mp4", "mkv", "mov", "wmv", "webm", "avi", "avchd", "3gp", "mpeg", "mpg"]
}

def check_is_file(file):
    """
    Checks if an input is a file or not
    """
    if os.path.isfile(file):
        return True
    return False

current_dir = os.getcwd()

for file_name in os.listdir('.'):
    checker = check_is_file(file_name)
    if checker == False:
        continue
    else:
        extension = file_name.split('.')[-1]
        for key,value in extensions.items():
            if extension in extensions[key]:
                shutil.move(os.path.join(current_dir, file_name), key)