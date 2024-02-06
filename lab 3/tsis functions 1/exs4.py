class Point:
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        print(self.x, self.y)

    def move(self , x ,y):
        self.x = x
        self.y = y

    def distance(self):
        print(((self.x**2) + (self.y**2)) ** 0.5)


point = Point(1,2)


point.show()
point.move(3,4)
point.show()
point.distance()
