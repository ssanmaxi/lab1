import re

text = input()
x = re.split(r'(?<=[a-z])(?=[A-Z])', text)
print(x)