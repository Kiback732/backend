import os
from api import api, log

def create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        log.debug(f'create directory {newpath}')
        os.makedirs(newpath)
    return newpath

def allowed_image(filename):
    if not "." in filename:
        log.error(f'no extension in {filename}')
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in api.config["ALLOWED_IMAGE_EXTENSIONS"]:
        log.debug(f'good extension in {filename}')
        return True
    else:
        log.error(f'bad extension in {filename}')
        return False
