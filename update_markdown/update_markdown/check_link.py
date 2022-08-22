from urllib import parse
import urllib.request
import urllib.error
from common import file_operation
from common import split_file
from common import re_pattern
from common import name


def lines_check_link(lines):
    # P_link, D_link
    pattern_objects = re_pattern.re_pattern_object_dict()
    generated_lines = []

    for line in lines:
        re_results = {pattern_name: pattern_object.search(repr(line))
                      for pattern_name, pattern_object in pattern_objects.items()}

        # linkの行の場合のみ、判定を実施し、末尾にコメントをつける

        if (re_results["P_link"] is None) and (re_results["D_link"] is None):
            generated_lines.append(line)
            continue

        re_result = re_results["P_link"] if re_results["P_link"] is not None else re_results["D_link"]
        result_dict = re_result.groupdict()

        add_comment = name.url_check_comment_ok if checkURL(parse.urljoin(
            "https://github.com/", result_dict["url"])) else name.url_check_comment_ng

        generated_lines.append(f"{line} %% {add_comment}")

    return generated_lines


def checkURL(url):
    try:
        f = urllib.request.urlopen(url)
        f.close()
        return True
    except:
        return False


def main():

    target_files_Path = file_operation.process_files_Path()
    backup_dir_Path = file_operation.backup_dir_Path()
    backup_dir_path = str(backup_dir_Path)

    file_operation.reset_dir(backup_dir_path)

    for file_Path in target_files_Path:
        if not file_Path.is_file():
            continue

        file_path = str(file_Path)

        lines = split_file.replace_lines(split_file.file_to_lines(file_path))

        new_lines = lines_check_link(lines)

        file_operation.update_file(new_lines, file_path, backup_dir_path)


if __name__ == '__main__':

    main()
