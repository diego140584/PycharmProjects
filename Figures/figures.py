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
        return "The object is %s and it's area is: x = %d, y = %d" % (self.__class__.__name__, self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Dot):
            return Line(Dot(self.x, self.y), Dot(other.x, other.y))
        elif isinstance(other, int):
            return Dot(self.x + other, self.y)
        elif isinstance(other, tuple):
            return Dot(self.x + other[0], self.y + other[1])


class Line(Figure):
    def __init__(self, d1, d2):
        self.dot1 = d1
        self.dot2 = d2
        super().__init__()

    def info(self):
        return "The New line was created with dots {} and {}.".format(self.dot1, self.dot2)

    def __str__(self):
        return "The New line was created with dots {} and {}.".format(self.dot1, self.dot2)

    def __add__(self, other):
        try:
            if isinstance(other, Dot):
                if self.dot1.x == other.x or self.dot1.y == other.y or self.dot2.x == other.x or self.dot2.y == other.y:
                    raise Exception

            elif isinstance(other, tuple):
                if self.dot1.x == other[0] or self.dot1.y == other[1] or self.dot2.x == other[0] or self.dot2.y == other[1]:
                    raise Exception

            elif isinstance(other, Line):
                k1 = (self.dot2.y - self.dot1.y) / (self.dot2.x - self.dot1.x)
                k2 = (other.dot2.y - other.dot1.y) / (other.dot2.x - other.dot1.x)
                if k1 == k2:
                    print(k1, k2)
                    raise Exception

        except Exception:
                print("{}".format(self, "Hi"))
        else:
            return Triangle(self.dot1, self.dot2, other)


class Triangle(Figure):
    def __init__(self, d1, d2, d3):
        self.dot1 = d1
        self.dot2 = d2
        self.dot3 = d3
        super().__init__()

class Rectangle(Figure):
    def __init__(self, d1, d2, d3, d4):
        self.dot1 = d1
        self.dot2 = d2
        self.dot3 = d3
        self.dot4 = d4
        super().__init__()


dot1 = Dot(1, 2)
dot2 = Dot(3, 4)
dot3 = Dot(5, 6)
dot4 = Dot(7, 8)

ln = Line(dot1, dot2)
ln2 = Line(dot3, dot4)
ln3 = ln + (1, 2)
print(ln3)
