class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag
    def add(self, c):
        s = Complex(self.r + c.r, self.i + c.i)
        return f"({self.r}+{self.i}j) + ({c.r}+{c.i}j) = ({s.r}+{s.i}j)"
    def input(self):
        self.r = float(input("Enter real part of c1: "))
        self.i = float(input('Enter imaginary part of c1: '))

c1 = Complex(0, 0)
c2 = Complex(0, 0)
c1.input()
c2.input()
print(c1.add(c2))