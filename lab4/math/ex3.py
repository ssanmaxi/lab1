import math
sides = int(input())
length = int(input())
area = float((1/4) * sides * length**2 * math.tan(math.pi / sides))
print(area)