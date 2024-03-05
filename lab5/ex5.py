import re

text = input()
x = re.findall(r"[a][b$]+", text)
print(x)