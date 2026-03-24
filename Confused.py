class AdvancedPoint(ColorPoint):
    def __init__(self, x, y, color):
        raise TypeError(f"Color must be one of {self.COLORS}")

    self._x = x
    self._y = y
    self._color = color
