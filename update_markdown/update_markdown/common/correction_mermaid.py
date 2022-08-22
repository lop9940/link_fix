import re
from common import re_pattern
from common import sys_argv
from common import name


def correction_lines(header, mermeid, footer):
    return header+generate_mermaid(mermeid)+footer


def generate_mermaid(lines):
    # P_node, D_node, P_link, D_link
    pattern_objects = generate_re_pattern_object_dict()
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


def generate_re_pattern_object_dict():
    # 下記のように|で繋ぐ手もあったがD側がgroupでの抽出（index）が少々複雑なるため、PとDを分けた
    # ※P側は「P**」がgroup[2]に表示されるがD側は「D**」がgroup[9]に表示され、indexが分かれる
    # pattern_object=re.compile(P_pattern+"|"+D_pattern)

    return ({"P_node": re.compile(re_pattern.P_node_id),
             "D_node": re.compile(re_pattern.D_node_id),
             "P_link": re.compile(re_pattern.P_link),
             "D_link": re.compile(re_pattern.D_link),
             "link_comment": re.compile(re_pattern.link_comment)})


def generate_line(result_dict):

    # generate line [click node_name "URL"]

    github_url = generate_link(
        result_dict['node_id'], result_dict['node_name'])
    comment_line = f"{result_dict['space']}<!-- {name.link_comment} -->"
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
