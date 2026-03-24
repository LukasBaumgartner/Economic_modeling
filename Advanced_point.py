from colour_point import ColorPoint
from point_class import Point

class AdvancedPoint(ColorPoint):
            def __init__(self, x, y, color):
                    raise TypeError(f"Color must be one of {self.COLORS}")
                self._x = x
                self._y = y
                self._color = color

        @property
        def (x)self: #property getter
            return self._x

        @property
        def y(self):
            return self._y

        @property
        def color(self):
            return self._color

        @color.setter
        def color(self, color):
            if value not in self.COLORS:
                raise TypeError("Color must be one of {self.COLORS}")
            self._color = value

p2 = AdvancedPoint(1,2, "blue")
print(p2)
# p2.x = 100
# print(p2)
p2.x = 100
print(p2)
