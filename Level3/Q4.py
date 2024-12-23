class Shape:
    def __init__(self):
        self.area = 0
    
    def Area(self):
        print(f" Area of Shape: {self.area}")
    
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def Area(self):
        self.area = self.length ** 2
        print(f" Area of Square: {self.area}")
    
shape = Shape()
shape.Area()

length = int(input(" Enter the length: "))
square = Square(length)
square.Area()