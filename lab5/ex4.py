import re

text = input()
x = re.findall(r"[A-Z][a-z]+", text)
print(x)
