import sys
import re
from unittest import result
import re_pattern
import name


def update_markdown(header, mermeid, footer):
    return header+generate_mermaid(mermeid)+footer


def generate_mermaid(lines):
    P_pattern_object, D_pattern_object = generate_re_pattern_object()
    generated_lines = []

    for line in lines:
        generated_lines.append(line)
        P_result = P_pattern_object.search(repr(line))
        D_result = D_pattern_object.search(repr(line))

        if (P_result is None) & (D_result is None):
            continue
        result = P_result if P_result is not None else D_result

        print(result.groupdict)

        generated_lines.append(generate_link_line(result.groupdict))

    return generated_lines


def generate_re_pattern_object():
    """
    下記のように|で繋ぐ手もあったがD側がgroupでの抽出（index）が少々複雑なるため、PとDを分けた
    ※P側は「P**」がgroup[2]に表示されるがD側は「D**」がgroup[9]に表示され、indexが分かれる

    pattern_object=re.compile(P_pattern+"|"+D_pattern)
    """
    P = re.compile(re_pattern.P_pattern)
    D = re.compile(re_pattern.D_pattern)
    return (P, D)

# add line [click node_name "URL"]


def generate_link_line(result_dict):
    """
    https://github.com/アカウント名/リポジトリ名/blob/ブランチ名/リポジトリからの相対パス.git
    sample:https://github.com/lop9940/link_fix/blob/feature/action_yaml_add_test/README.md
    """

    github_url = generate_link(result_dict['node_id'],result_dict['node_name'])
    return f"{result_dict['space']}click {result_dict['node_id']} \"{github_url}\""


def generate_link(node_id, node_name):

    repository = sys.argv[1]  # ${{ github.repository }}
    blob = name.blob
    branch = sys.argv[2]  # ${{ github.ref_name }}
    dir = name.P_dir if "p" in node_id else name.D_dir
    file = node_name+".md"
    return "/".join([repository, blob, branch, dir, file])
