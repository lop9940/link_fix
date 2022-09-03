import os
import shutil
import pathlib
from common import name


def reset_dir(dir_path):

    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)


def get_process_files_Path():

    return pathlib.Path(name.P_dir).iterdir()


def get_backup_dir_Path():

    return pathlib.Path(name.backup_dir)


def update_file(lines, target_file_path, backup_dir_path):

    shutil.copy(target_file_path, backup_dir_path)

    with open(target_file_path, "w") as file:
        file.write("\n".join(lines))
