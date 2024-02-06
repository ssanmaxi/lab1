class Shape:
    def area(self):
        print(0)


class Rectangle(Shape):
    length = 0
    width = 0

    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

q = Rectangle(12,6)
q.area()
