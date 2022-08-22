import re
from common import file_operation
from common import split_file
from common import re_pattern
from common import sys_argv
from common import name


def generate_mermaid(lines):
    # P_node, D_node, P_link, D_link
    pattern_objects = re_pattern.correction_object_dict()
    generated_lines = []

    for line in lines:
        re_results = {pattern_name: pattern_object.search(repr(line))
                      for pattern_name, pattern_object in pattern_objects.items()}

        # node idの行の場合、その行を追加し、合わせてリンクも挿入
        # linkの行の場合、その行は追加しない
        # どちらの行でもない場合、その行のみを追加

        if ((re_results["P_link"] is not None) or (re_results["D_link"] is not None)
                or (re_results["link_comment"] is not None)):
            continue
        generated_lines.append(line)
        if (re_results["P_node"] is None) and (re_results["D_node"] is None):
            continue
        re_result = re_results["P_node"] if re_results["P_node"] is not None else re_results["D_node"]

        generated_lines.append(generate_line(re_result.groupdict()))

    return generated_lines


def generate_line(result_dict):

    # generate line [click node_name "URL"]

    github_url = generate_link(
        result_dict['node_id'], result_dict['node_name'])
    comment_line = f"{result_dict['space']}%% {name.link_comment}"
    link_line = f"{result_dict['space']}click {result_dict['node_id']} \"{github_url}\""
    return f"{comment_line}\n{link_line}"


def generate_link(node_id, node_name):

    # https://github.com/アカウント名/リポジトリ名/blob/ブランチ名/リポジトリからの相対パス.git
    # sample:https://github.com/lop9940/link_fix/blob/feature/action_yaml_add_test/README.md

    repository = sys_argv.repository_name
    blob = name.blob
    branch = sys_argv.branch_name
    dir = name.P_dir if "p" in node_id else name.D_dir
    file = node_name+".md"
    return "/".join([repository, blob, branch, dir, file])


def main():

    target_files_Path = file_operation.process_files_Path()
    backup_dir_Path = file_operation.backup_dir_Path()
    backup_dir_path = str(backup_dir_Path)

    file_operation.reset_dir(backup_dir_path)

    for file_Path in target_files_Path:
        if not file_Path.is_file():
            continue

        file_path = str(file_Path)

        header, mermeid, footer = split_file.split_file(file_path)

        new_lines = header+generate_mermaid(mermeid)+footer

        file_operation.update_file(new_lines, file_path, backup_dir_path)


if __name__ == "__main__":
    main()
