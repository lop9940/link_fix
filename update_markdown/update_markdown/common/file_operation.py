import os
from pprint import pprint
import shutil
import pathlib
from common import name

def reset_dir(dir_path):
    shutil.rmtree(dir_path)
    os.mkdir(dir_path)

def process_files_Path():

    process_dir_Path = pathlib.Path(name.P_dir)
    print("process_dir_Path:")
    pprint(type(process_dir_Path))
    pprint(process_dir_Path.iterdir)
    return process_dir_Path.iterdir()

def backup_dir_Path():

    print("backup_dir_Path:")
    print(pathlib.Path(name.backup_dir))
    return pathlib.Path(name.backup_dir)