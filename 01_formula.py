# quadratic equation,

#https://www.wikihow.com/Solve-Quadratic-Equations
#https://www.programiz.com/python-programming/examples/quadratic-roots
# ax2 +bx+c =0

# x1 = (-b+(b2-4ac)**2)/2a

# x2 = (-b+(b2-4ac)**2)/2a


import cmath
class quadratic_equation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def find_sqr(self):
        self.q = (self.b**self.b -4*self.a*self.c)
        return self.q
    def x1_x2(self):
        x1 = (-self.b + cmath.sqrt(self.q) / (2 * self.a))
        x2 = (-self.b - cmath.sqrt(self.q) / (2 * self.a))
        return x1, x2






qe = quadratic_equation(3,-5,-8)
qe1= quadratic_equation(1,5,6)
print(qe.find_sqr())

print(qe.x1_x2())
print(qe1.x1_x2())

