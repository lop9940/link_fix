import os
import re
import shutil
import sys
from turtle import back
import re_pattern
import name
import search_target


def main():
    target_file_path = "{name.P_dir}/{name.target_file_name}"
    backup_file_path = "{name.backup_dir}/{name.target_file_name}"

    header, mermeid, footer = file_lines_split(target_file_path)

    new_lines = generate_markdown_lines(header, mermeid, footer)

    file_updata(target_file_path, backup_file_path, new_lines)


def file_lines_split(file_path):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    lines_replace = [line.replace('\n', '') for line in lines]
    mermaid_first_index = index_search(
        lines_replace, search_target.first_target)
    remaining_lines = lines_replace[mermaid_first_index:]
    mermaid_last_lindex = index_search(
        lines_replace, search_target.last_target)

    header_lines = lines_replace[:mermaid_first_index-1]
    mermeid_lines = remaining_lines[:mermaid_last_lindex]
    footer_lines = remaining_lines[mermaid_last_lindex+1:]

    return (header_lines, mermeid_lines, footer_lines)


def index_search(list, target, default=False):
    return list.index(target) if target in list else default


def generate_markdown_lines(header, mermeid, footer):
    return header+generate_mermaid_lines(mermeid)+footer


def generate_mermaid_lines(lines):
    P_pattern_object, D_pattern_object = re_pattern_object()
    generate_lines = []

    for line in lines:
        generate_lines.append(line)
        P_result = P_pattern_object.search(repr(line))
        D_result = D_pattern_object.search(repr(line))

        if (P_result is None) & (D_result is None):
            continue
        if P_result is not None:
            add_line = generate_line(P_result)
        elif D_result is not None:
            add_line = generate_line(D_result)

        generate_lines.append(add_line)
    return generate_lines

# 下記のように|で繋ぐ手もあったがD側がgroupでの抽出（index）が少々複雑なるため、PとDを分けた
# ※P側は「P**」がgroup[2]に表示されるがD側は「D**」がgroup[9]に表示され、indexが分かれる
# pattern_object=re.compile(P_pattern+"|"+D_pattern)


def re_pattern_object():
    P = re.compile(re_pattern.P_pattern)
    D = re.compile(re_pattern.D_pattern)
    return (P, D)

# add line [click node_name "URL"]


def generate_line(result):

    node_id = result.group(2)
    node_name = result.group(4)
    dir = name.P_dir if "p" in node_id else name.D_dir
    file = node_name+".md"
    github_url = "/".join([git_url_nofile(), dir, file])
    return result.group(1)+"click "+node_id+" \""+github_url+"\""

# https://github.com/アカウント名/リポジトリ名.git
# https://github.com/lop9940/link_fix/blob/feature/action_yaml_add_test/README.md


def git_url_nofile():
    repository = sys.argv[1]  # ${{ github.repository }}
    branch = sys.argv[2]  # ${{ github.ref_name }}
    return "/".join([repository, "blob", branch])


def file_updata(target_file_path, backup_file_path, new_lines):
    shutil.rmtree(name.backup_dir)
    os.mkdir(name.backup_dir)
    shutil.copy(target_file_path, backup_file_path)

    with open(target_file_path, "w") as file:
        file.write("\n".join(new_lines))


if __name__ == "__main__":
    main()
