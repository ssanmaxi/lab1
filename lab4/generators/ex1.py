a = int(input())
def generate_squares(a):
    for i in range(1, a+1):
        yield i**2
squares_generator = generate_squares(a)
for square in squares_generator:
    print(square)