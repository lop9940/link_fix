import pathlib
import name
from split_file import split_file
from update_markdown import update_markdown
from update_file import update_file


def main():

    process_dir_Path = pathlib.Path("process")
    target_files_Path = process_dir_Path.iterdir()
    backup_dir_path = str(pathlib.Path("backup"))

    for file_Path in target_files_Path:
        if not file_Path.is_file():
            continue

        header, mermeid, footer = split_file(str(file_Path))

        new_lines = update_markdown(header, mermeid, footer)

        print(new_lines)

        # update_file(file_path, backup_path, new_lines)


if __name__ == "__main__":
    main()
