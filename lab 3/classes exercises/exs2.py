class Shape:
    def area(self):
        print(0)


class Square(Shape):
    side = 0

    def __init__(self, side):
        self.side = side

    def area(self):
        print(self.side ** 2)


q = Square(12)

q.area()
