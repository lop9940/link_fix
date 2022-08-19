import sys
import re
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
        if P_result is not None:
            add_line = generate_link_line(P_result)
        elif D_result is not None:
            add_line = generate_link_line(D_result)

        generated_lines.append(add_line)

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


def generate_link_line(result):
    """
    https://github.com/アカウント名/リポジトリ名/blob/ブランチ名/リポジトリからの相対パス.git
    sample:https://github.com/lop9940/link_fix/blob/feature/action_yaml_add_test/README.md
    """

    node_id = result.group(2)
    node_name = result.group(4)
    dir = name.P_dir if "p" in node_id else name.D_dir
    file = node_name+".md"
    github_url = "/".join([git_url_nofile(), dir, file])
    return f"{result.group(1)}click {node_id} \"{github_url}\""


def git_url_nofile():
    repository = sys.argv[1]  # ${{ github.repository }}
    branch = sys.argv[2]  # ${{ github.ref_name }}
    return "/".join([repository, "blob", branch])

