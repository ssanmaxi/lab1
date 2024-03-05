import re

text = input()
x = re.sub(r"[ -.,]", ":", text)
print(x)