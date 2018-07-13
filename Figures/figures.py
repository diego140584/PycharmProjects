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
                if (other.x - self.dt1.x) / (self.dt2.x - self.dt1.x) == \
                        (other.y - self.dt1.y) / (self.dt2.y - self.dt1.y):
                    raise Exception
                    # Проверка на параллельность отрезков
            elif isinstance(other, Line):
                k1 = (self.dt2.y - self.dt1.y) / (self.dt2.x - self.dt1.x)
                k2 = (other.dt2.y - other.dt1.y) / (other.dt2.x - other.dt1.x)
                if k1 == k2:  # проверка на принадлежность точек второму отрезку
                    if ((other.dt1.x - self.dt1.x) / (other.dt1.y - self.dt1.y) == \
                        (other.dt1.x - self.dt2.x) / (other.dt1.y - self.dt2.y)) \
                            or ((other.dt2.x - self.dt1.x) / (other.dt2.y - self.dt1.y) == \
                                (other.dt2.x - self.dt2.x) / (other.dt2.y - self.dt2.y)):
                        raise Exception


        except Exception:
            if other.info() == "Dot":
                return "The dot located the same area, triangle can't create."
            else:
                return "The line is on the current line, rectangle can't create!"
        else:
            if other.info() == "Dot":
                return Triangle(self.dt1, self.dt2, other)
            else:
                if k1 == k2:
                    fg = Rectangle(self.dt1, self.dt2, other.dt1, other.dt2)
                    fg.trapeze = True
                    return fg


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
    trapeze = False

    def __init__(self, d1, d2, d3, d4):
        self.dot1 = d1
        self.dot2 = d2
        self.dot3 = d3
        self.dot4 = d4
        super().__init__()

    def info(self):
        d1 = math.sqrt((self.dot2.x - self.dot1.x) ** 2 + (self.dot2.y - self.dot1.y) ** 2)
        d2 = math.sqrt((self.dot3.x - self.dot2.x) ** 2 + (self.dot3.y - self.dot2.y) ** 2)
        d3 = math.sqrt((self.dot4.x - self.dot3.x) ** 2 + (self.dot4.y - self.dot3.y) ** 2)
        d4 = math.sqrt((self.dot4.x - self.dot1.x) ** 2 + (self.dot4.y - self.dot1.y) ** 2)
        dg1 = math.sqrt((self.dot4.x - self.dot2.x) ** 2 + (self.dot4.y - self.dot2.y) ** 2)
        dg2 = math.sqrt((self.dot3.x - self.dot1.x) ** 2 + (self.dot3.y - self.dot1.y) ** 2)

        if d1 == d2 == d3 == d4 and self.trapeze:
            return "The figure is trapeze with lenghts: First - %d,\
Second - %d, Third - %d, fourth - %d" % (d1, d2, d3, d4)
        elif d1 == d2 == d3 == d4:
            return "The figure is squire.with the same fourth lenghts: First - %d." % (d1)
        elif dg1 == dg2:
            return "The figure is rectangle with lenghts: First - %d,\
Second - %d, Third - %d, fourth - %d" % (d1, d2, d3, d4)
        elif 4 * (d1 ** 2) == (dg1 ** 2) + (dg2 ** 2):
            return "The figure is rhombus with lenghts: First - %d,\
Second - %d, Third - %d, fourth - %d" % (d1, d2, d3, d4)
        elif self.trapeze:
            return "The figure is trapeze with lenghts: First - %d,\
Second - %d, Third - %d, fourth - %d" % (d1, d2, d3, d4)


if __name__ == "__main__":
    t1 = Dot(1, 1)
    t2 = Dot(5, 5)
    t3 = Dot(3, 3)
    t4 = Dot(6, 6)
    ln = t1 + t2
    ln2 = t3 + t4
    rec = ln + ln2
    try:
        print(rec.info())
    except:
        print("The object wasn't create.")
