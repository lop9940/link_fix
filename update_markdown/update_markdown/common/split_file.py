from common import search_target


def split_file(file_path):
    lines = file_to_lines(file_path)

    header_lines, mermeid_lines, footer_lines = split_lines(
        replace_lines(lines))

    return (header_lines, mermeid_lines, footer_lines)


def file_to_lines(path):
    with open(path, 'r') as file:
        return file.readlines()


def replace_lines(lines):
    return [line.replace('\n', '') for line in lines]


def split_lines(lines):
    mermaid_first_index = search_index(
        lines, search_target.first_target)
    remaining_lines = lines[mermaid_first_index:]
    mermaid_last_lindex = search_index(
        lines, search_target.last_target)

    header = lines[:mermaid_first_index]
    mermeid = remaining_lines[:mermaid_last_lindex]
    footer = remaining_lines[mermaid_last_lindex+1:]

    return header, mermeid, footer


def search_index(list, target, default=False):
    return list.index(target) if target in list else default
