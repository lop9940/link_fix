import os
import shutil
import name


def update_file(target_file_path, backup_file_path, new_lines):
    shutil.rmtree(name.backup_dir)
    os.mkdir(name.backup_dir)
    shutil.copy(target_file_path, backup_file_path)

    with open(target_file_path, "w") as file:
        file.write("\n".join(new_lines))
