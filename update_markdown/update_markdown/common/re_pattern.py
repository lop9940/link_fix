import re
from common import name

def re_pattern_object_dict():
    return ({"P_link": re.compile(P_link),
             "D_link": re.compile(D_link)})

P_node_id = "(?P<space>\s*?)(?P<node_id>p\d+)(?P<node_start>\(\[)(?P<node_name>.*?)(?P<node_end>\]\))"
D_node_id = "(?P<space>\s*?)(?P<node_id>d\d+)(?P<node_start>\[/)(?P<node_name>.*?)(?P<node_end>/\])"
P_link = "(?P<space>\s*?)(?P<click>click\s)(?P<node_id>p\d+)(?P<url_start>\s\")(?P<url>.*?)(?P<url_end>\")"
D_link = "(?P<space>\s*?)(?P<click>click\s)(?P<node_id>d\d+)(?P<url_start>\s\")(?P<url>.*?)(?P<url_end>\")"
link_comment = name.link_comment
