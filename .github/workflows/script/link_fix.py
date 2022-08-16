import os
import re
import shutil

def file_lines_split(file_path,first_index_target,last_index_target):

  with open(file_path, 'r') as file:
    lines = file.readlines()

  lines_replace = [line.replace('\n', '') for line in lines]
  mermaid_first_index=index_search(lines_replace,first_index_target)
  remaining_lines=lines_replace[mermaid_first_index:]
  mermaid_last_lindex=index_search(lines_replace,last_index_target)

  header_lines=lines_replace[:mermaid_first_index-1]
  mermeid_lines=remaining_lines[:mermaid_last_lindex]
  footer_lines=remaining_lines[mermaid_last_lindex+1:]

  return(header_lines,mermeid_lines,footer_lines)

def index_search(list, target, default=False):
  return list.index(target) if target in list else default

def generate_mermaid_lines(lines):
    P_pattern_object,D_pattern_object=re_pattern_object()
    generate_lines=[]

    for line in lines:
      generate_lines.append(line)
      P_result=P_pattern_object.search(repr(line))
      D_result=D_pattern_object.search(repr(line))

      if (P_result is None) & (D_result is None):continue
      if P_result is not None:
        add_line=generate_line(P_result)
      elif D_result is not None:
        add_line=generate_line(D_result)

      generate_lines.append(add_line)
    return generate_lines

# 下記のように|で繋ぐ手もあったがD側がgroupでの抽出（index）が少々複雑なるため、PとDを分けた
# ※P側は「P**」がgroup[2]に表示されるがD側は「D**」がgroup[9]に表示され、indexが分かれる
# pattern_object=re.compile(P_pattern+"|"+D_pattern)

def re_pattern_object():
  P_pattern,D_pattern=re_pattern()
  P=re.compile(P_pattern)
  D=re.compile(D_pattern)
  return(P,D)

# add line [click node_name "URL"]

def generate_line(result):

  node_id=result.group(2)
  node_name=result.group(4)
  file=node_id+"_"+node_name+".md"
  github_url="/".join([git_url_nofile(),file])
  return result.group(1)+"click "+node_id+" \""+github_url+"\""

# https://github.com/アカウント名/リポジトリ名.git
# https://github.com/lop9940/markdown_deliverable/blob/add-github-actions-yaml/D01_dTest1.md

def git_url_nofile():
  http="https://github.com"
  account="lop9940"# 後入
  repository="markdown_deliverable"# 後入
  blob="blob"
  branch="add-github-actions-yaml"# 後入
  return "/".join([http,account,repository,blob,branch])

def re_pattern():
  P="(\s*?)(P\d+)(\(\[)(.*?)(\]\))"
  D="(\s*?)(D\d+)(\[/)(.*?)(/\])"
  return(P,D)



header,mermeid,footer=file_lines_split("P01_test.md","```mermaid","```")

new_mermaid = generate_mermaid_lines(mermeid) 

new_lines=header+new_mermaid+footer

shutil.rmtree("backup")
os.mkdir("backup")
shutil.copy("P01_test.md","backup/P01_test_backup.md")

with open("P01_test.md", "w") as file:
  file.write("\n".join(new_lines))