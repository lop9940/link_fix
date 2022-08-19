import search_target


def split_file(file_path):
    lines = file_to_lines(file_path)

    header_lines, mermeid_lines, footer_lines = split_lines(lines)

    return (header_lines, mermeid_lines, footer_lines)


def file_to_lines(path):
    with open(path, 'r') as file:
        return file.readlines()


def split_lines(lines):
    lines_replace = [line.replace('\n', '') for line in lines]

    mermaid_first_index = search_index(
        lines_replace, search_target.first_target)
    remaining_lines = lines_replace[mermaid_first_index:]
    mermaid_last_lindex = search_index(
        lines_replace, search_target.last_target)

    header = lines_replace[:mermaid_first_index-1]
    mermeid = remaining_lines[:mermaid_last_lindex]
    footer = remaining_lines[mermaid_last_lindex+1:]

    return header, mermeid, footer


def search_index(list, target, default=False):
    return list.index(target) if target in list else default
