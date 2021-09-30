import math
class Figure:
    def __init__(self):
        pass

    @property
    def s(self):
        pass

    @property
    def p(self):
        pass

class Quadrilateral(Figure):
    def __init__(self, side1, side2, side3, side4, diag1, diag2, ang):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4
        self.diag1 = diag1
        self.diag2 = diag2
        self.ang = ang

    @property
    def p(self, side1, side2, side3, side4):
        return self.side1 + self.side2 + self.side3 + self.side4

    @property
    def s(self, diag1, diag2, ang):
        return 0.5 * diag1 * diag2 * math.sin(math.radians(ang))

class Parallelogram(Quadrilateral):
    def __init__(self, *args):
        super().__init__(*args)

    @property
    def p(self, side1, side2, side3, side4):
        super().p(side1, side2, side3, side4)

    @property
    def s(self, p, side1, side2, diag1):
        a = (self.side1 + self.side2 + self.diag1) / 2
        return 2 * (0.5 ** (a * (a - self.side1) * (a - self.side2) * (a - self.diag1)))

class Rhombus(Parallelogram):
    def __init__(self, side1, diag1, diag2):
        super().__init__(side1, side1, side1, side1, diag1, diag2, ang=None)

    @property
    def p(self, side1):
        return 4 * self.side1

    @property
    def s(self, diag1, diag2):
        return (self.diag1 * self.diag2) / 2

class Rectagle(Quadrilateral):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def p(self, length, width):
        super().p(length, width, length, width)

    @property
    def s(self, length, width):
        return self.length * self.width

class Square(Rhombus):
    def __init__(self, side1):
        self.side1 = side1

    @property
    def p(self, side1):
        super().p(side1)

    @property
    def s(self, side1):
        return self.side1 * self.side1

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def p(self, side1, side2, side3):
        return self.side1 + self.side2 + self.side3

    @property
    def s(self, p, side1, side2, side3):
        a = self.p / 2
        return a * (a - self.side1) * (a - self.side2) * (a - self.side3)

class IsoscelesTriangle(Triangle):
    def __init__(self, side1, side3):
        super().__init__(side1, side1, side3)

    @property
    def p(self, side1, side3):
        return 2 * self.side1 + self.side3

    @property
    def s(self, p, side1, side3):
        super().s(p, side1, side2= side1, side3)

class EquilaeralTriangle(Triangle):
    def __init__(self, side):
        self.side = side

    @property
    def p(self, side):
        return self.side * 3

    @property
    def s(self, side):
        return (self.side ** 2 * math.sqrt(3)) / 4

class Circle(Figure):
    def __init__(self, rad):
        self.rad = rad

    @property
    def s(self, rad):
        return math.pi * (self.rad ** 2)

    @property
    def p(self, rad):
        return 2 * math.pi * self.rad

class Oval(Circle):
    def __init__(self, big_d, small_d):
        self.big_d = big_d
        self.small_d = small_d

    @property
    def s(self, big_d, small_d):
        return math.pi * self.big_d * self.small_d

    @property
    def p(self, big_d, small_d):
        return 2 * math.pi * math.sqrt((self.small_d ** 2 + self.big_d ** 2) / 2)

def s(figure):
    return figure.s

def p(figure):
    return figure.p
