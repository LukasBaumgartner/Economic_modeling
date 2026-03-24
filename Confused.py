class AdvancedPoint(ColorPoint):
    """
    Advanced Class showcasing class concepts
    """
    COLORS = ["red", "green", "blue", "black", "white", "yellow"]
#     capitalized to show class attributes
    def __init__(self, x, y, color):
        if not isinstance(x, (int, float)):
            raise TypeError("x must be int or float")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be int or float")
        if Color not in self.COLORS:
            raise TypeError("Color must be one of {self.COLORS)")
        self.x = x
        self.y = y
        self.color = color