import math


class Figure:
    def __init__(self):
        pass

    def info(self):
        pass

    def property(self):
        pass


class Dot(Figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__()

    def __str__(self):
        return "The dot's position is: x = %d, y = %d" % (self.x, self.y)

    def info(self):
        return self.__class__.__name__

    def __add__(self, other):
        if isinstance(other, Dot):
            return Line(Dot(self.x, self.y), Dot(other.x, other.y))
        elif isinstance(other, int):
            return Dot(self.x + other, self.y)
        elif isinstance(other, tuple):
            return Dot(self.x + other[0], self.y + other[1])


class Line(Figure):
    def __init__(self, d1, d2):
        self.dt1 = d1
        self.dt2 = d2
        super().__init__()

    def info(self):
        return self.__class__.__name__

    def __str__(self):
        return "The New line was created with dots {} and {}.".format(self.dt1, self.dt2)

    def __add__(self, other):
        try:
            if isinstance(other, Dot):
                if ((other.x - self.dt1.x) * (self.dt2.y - self.dt1.y) * (self.dt2.x - self.dt1.x) \
                    * (other.y - self.dt1.y)) == 0:
                    raise Exception

            elif isinstance(other, Line):
                k1 = (self.dt2.y - self.dt1.y) / (self.dt2.x - self.dt1.x)
                k2 = (other.dt2.y - other.dt1.y) / (other.dt2.x - other.dt1.x)
                if k1 == k2:
                    print("The new line is parallel to current")
                else:
                    b1 = self.dt1.y - k1 * self.dt1.x
                    b2 = other.dt1.y - k2 * other.dt1.x
                    x = (b1 - b2) / (k1 - k2)
                    y = k2 * x + b2
                    if (self.dt1.x <= other.dt2.x <= self.dt2.x) or \
                            (self.dt1.x <= other.dt1.x <= self.dt2.x):
                        raise Exception

        except Exception:
            if other.info() == "Dot":
                return "The dot located the same area, triangle can't create."
            else:
                return "The line intersected the current line, rectangle can't create!"
        else:
            if other.info() == "Dot":
                return Triangle(self.dt1, self.dt2, other)
            else:
                return Rectangle(self.dt1, self.dt2, other.dt1, other.dt2)


class Triangle(Figure):
    def __init__(self, d1, d2, d3):
        self.dot1 = d1
        self.dot2 = d2
        self.dot3 = d3
        super().__init__()

    def info(self):
        d1 = math.sqrt((self.dot2.x - self.dot1.x) ** 2 + (self.dot2.y - self.dot1.y) ** 2)
        d2 = math.sqrt((self.dot3.x - self.dot2.x) ** 2 + (self.dot3.y - self.dot2.y) ** 2)
        d3 = math.sqrt((self.dot3.x - self.dot1.x) ** 2 + (self.dot3.y - self.dot1.y) ** 2)
        if d1 == d2 or d2 == d3 or d1 == d3:
            return "The created triangle is isosceles"
        else:
            return "The created triangle is versatile"


class Rectangle(Figure):
    def __init__(self, d1, d2, d3, d4):
        self.dot1 = d1
        self.dot2 = d2
        self.dot3 = d3
        self.dot4 = d4
        super().__init__()


t1 = Dot(1, 1)
t2 = Dot(4, 5)
t3 = Dot(4, 1)
t4 = Dot(7, 5)
l1 = Line(t1, t2)
l2 = Line(t3, t4)
l3 = l1 + l2
tr = l1 + t4
print(l3)
print(tr.info())
