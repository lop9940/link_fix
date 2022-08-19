import os
import shutil
import pathlib
import name
from split_file import split_file
from update_markdown import update_markdown
from update_file import update_file


def main():

    process_dir_Path = pathlib.Path(name.P_dir)
    target_files_Path = process_dir_Path.iterdir()
    backup_dir_path = str(pathlib.Path(name.backup_dir))
    shutil.rmtree(backup_dir_path)
    os.mkdir(backup_dir_path)

    for file_Path in target_files_Path:
        if not file_Path.is_file():
            continue

        file_path = str(file_Path)

        header, mermeid, footer = split_file(file_path)

        new_lines = update_markdown(header, mermeid, footer)

        print(new_lines)

        update_file(new_lines, file_path, backup_dir_path)


if __name__ == "__main__":
    main()
