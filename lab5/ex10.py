import re

text = input()
x = re.sub(r'(?<=[a-z])(?=[A-Z])', r'_' , text)
print(x)




