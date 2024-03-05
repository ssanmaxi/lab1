import re

a = str(input())

def check(a):
    ch = r'ab*'
    if re.match(ch, a):
        return True
    else:
        return False

for i in a:
    print(f"{i}:({check(a)})")