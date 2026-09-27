class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloads binary addition '+'
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloads scalar multiplication '*'
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # Overloads floor division '//'
    def __floordiv__(self, scalar):
        return Vector(self.x // scalar, self.y // scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(4, 8)
v2 = Vector(2, 3)

print(v1 + v2)   # Output: Vector(6, 11)
print(v1 * 3)    # Output: Vector(12, 24)
print(v1 // 2)   # Output: Vector(2, 4)