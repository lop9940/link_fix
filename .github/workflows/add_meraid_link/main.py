import name
from split_file import split_file
from update_markdown import update_markdown
from update_file import update_file


def main():

    for file_name in name.target_files:
        file_path = f"{name.P_dir}/{file_name}"
        backup_path = f"{name.backup_dir}/{file_name}"

        header, mermeid, footer = split_file(file_path)

        new_lines = update_markdown(header, mermeid, footer)

        print(new_lines)

        update_file(file_path, backup_path, new_lines)


if __name__ == "__main__":
    main()
