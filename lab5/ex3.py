import re

text = input()
x = re.findall(r"[a-z]+_[a-z]+", text)
print(x)
