import pathlib
import name
from split_file import split_file
from update_markdown import update_markdown
from update_file import update_file


def main():

    process_path=pathlib.Path("process")
    target_files_path=[str(p) for p in process_path.iterdir() if p.is_file()] 

    for path in target_files_path:
        # backup_path = f"{name.backup_dir}/{file_name}"

        header, mermeid, footer = split_file(path)

        new_lines = update_markdown(header, mermeid, footer)

        print(new_lines)

        # update_file(file_path, backup_path, new_lines)


if __name__ == "__main__":
    main()
