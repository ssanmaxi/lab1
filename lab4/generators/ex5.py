a = int(input())

def generator_reverse(a):
    for i in range(a, -1, -1):
        yield i
reverse = generator_reverse(a)
for i in reverse:
    print(i)