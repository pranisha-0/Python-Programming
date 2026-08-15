class Rectangle:
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth
    def area(self):
        return f"area: {self.l * self.b}"
    def perimeter(self):
            return f"perimter:  {2 * (self.l + self.b)}"
    def input(self):
        self.l = float(input("Enter length: "))
        self.b = float(input("ENter breadth: "))
r1 = Rectangle(0, 0)
r1.input()
print(r1.area())
print(r1.perimeter())