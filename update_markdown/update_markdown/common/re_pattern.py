import re
import name


def all_re_patterns():
    return {"P_node_id": "(?P<space>\s*?)(?P<node_id>p\d+)(?P<node_start>\(\[)(?P<node_name>.*?)(?P<node_end>\]\))",
            "D_node_id": "(?P<space>\s*?)(?P<node_id>d\d+)(?P<node_start>\[/)(?P<node_name>.*?)(?P<node_end>/\])",
            "P_link": "(?P<space>\s*?)(?P<click>click\s)(?P<node_id>p\d+)(?P<url_start>\s\")(?P<url>.*?)(?P<url_end>\")",
            "D_link": "(?P<space>\s*?)(?P<click>click\s)(?P<node_id>d\d+)(?P<url_start>\s\")(?P<url>.*?)(?P<url_end>\")",
            "link_comment": name.link_comment}


def check_re_pattern_names():
    return ["P_link", "D_link"]


def check_object_dict():
    return (make_object_dict(check_re_pattern_names, all_re_patterns))


def make_object_dict(re_pattern_names, re_patterns_dict):
    return {pattern_name: re.compile(re_pattern) for pattern_name,
            re_pattern in re_patterns_dict.items() if pattern_name in re_pattern_names}
