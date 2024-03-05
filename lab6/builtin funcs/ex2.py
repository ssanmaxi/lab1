import math

a = str(input())

upper = sum(1 for i in a if i.isupper())
lower = sum(1 for i in a if i.islower())

print(upper)
print(lower)