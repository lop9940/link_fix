import name
from split_file import split_file
from update_markdown import update_markdown
from update_file import update_file


def main():
    header, mermeid, footer = split_file(name.target_file_path)

    new_lines = update_markdown(header, mermeid, footer)

    update_file(name.target_file_path, name.backup_file_path, new_lines)


if __name__ == "__main__":
    main()
