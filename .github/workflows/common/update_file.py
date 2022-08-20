import shutil


def update_file(lines, target_file_path, backup_dir_path):

    shutil.copy(target_file_path, backup_dir_path)

    with open(target_file_path, "w") as file:
        file.write("\n".join(lines))
