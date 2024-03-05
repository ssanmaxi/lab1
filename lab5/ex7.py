import re

text = input()
x = re.sub(r"_[a-z]", lambda y: y.group(0)[1].upper(), text)
print(x)