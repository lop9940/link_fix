import pathlib

p = pathlib.Path('.')
p_rel=pathlib.Path('../../P01_test.md')
a_rel=pathlib.Path("..")


print(p.cwd())
print(p_rel.resolve())
print(a_rel.resolve())