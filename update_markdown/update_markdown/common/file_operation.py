import os
import shutil
import pathlib
from common import name

def reset_dir(dir_path):
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)

def process_files_Path():

    process_dir_Path = pathlib.Path(name.P_dir)
    return process_dir_Path.iterdir()

def backup_dir_Path():

    return pathlib.Path(name.backup_dir)

def update_file(lines, target_file_path, backup_dir_path):

    shutil.copy(target_file_path, backup_dir_path)

    with open(target_file_path, "w") as file:
        file.write("\n".join(lines))
