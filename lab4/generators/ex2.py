a = int(input())
def generate_evens(a):
    for i in range(0, a+1, 2):
            yield i
evens = generate_evens(a)
print(*evens, sep=", ")