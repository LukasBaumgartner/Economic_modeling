from Session_2_colour import ColorPoint
from session_1 import (Point)


class AdvancedPoint(ColorPoint):
    """
    Advanced Class showcasing class concepts
    """
    COLORS = ["red", "green", "blue", "black", "white", "yellow"]

    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        if color not in self.COLORS:
            raise TypeError(f"Color must be one of {self.COLORS}")

        self._x = x
        self._y = y
        self._color = color

    def __str__(self):
        return f"p<{self.x}, {self.y}, {self.color}>"

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be int or float")
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be int or float")
        self._y = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value not in self.COLORS:
            raise TypeError(f"Color must be one of {self.COLORS}")
        self._color = value

    @classmethod
    def add_color(cls, color):
        cls.COLORS.append(color)

    @staticmethod
    def distance_2_points(p1, p2): #This does not access any attributes
        return p1.origin(p2)

    @staticmethod
    def from_string(text):
        # I want to create an advanced point from a string: "red 2 7"
        # Also called a "factory" method!
        color, x, y = text.split()
        if color not in AdvancedPoint.COLORS:
            raise TypeError(f"Color must be one of {AdvancedPoint.COLORS}")
        x=float(x)
        y=float(y)
        return AdvancedPoint(x,y,color)
p2 = AdvancedPoint(1, 2, "blue")
print(p2)
p2.x = 100
print(p2)
p2.color = "red"
print(AdvancedPoint.COLORS)
p1 = Point(0,0)
print(AdvancedPoint.distance_2_points(p1, p2))

# A class can have regular methods, with instant attributes for the class. They have magic methods.
# Innit - when I create an instance
#w_lt when I want to make the less than comparison between myself and another element
# If you want to multiply yourself, mul - multiply

p2 = AdvancedPoint.from_string("pink 7 6.2")
print(p2)