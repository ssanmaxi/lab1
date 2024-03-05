import re

def check(string):
    ch = r'ab{2,3}'
    if re.search(ch, string):
        return True
    else :
        return False

test = ("cf")

for i in test:
    print(f"{i}: ({check(test)})")
