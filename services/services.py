import os
import shutil
from fastapi import UploadFile


def write_image(file_name: str, file: UploadFile):
    with open(file_name, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)


def delete_old_file(path_file):
    if os.path.exists(path_file):
        os.remove(path_file)