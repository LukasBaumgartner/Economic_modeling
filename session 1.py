class Point:
    def __init__(self, x: object, y: object) -> None:
        """
        Initialize the point
        :param x: x-coordinate
        :param y: y-coordinate
        """
        self.x = x
        self.y = y
    def __str__(self):
        """
        Return a string presentation of the point
        :return: p<x, y>
        """
        return f"p<{self.x}, {self.y}>"
    def __repr__(self):
        return self.__str__()

    def distance_origin(self):
        """
        Return the distance from origin to the point
        :return: float
        """
        return (self.x**2 + self.y**2)**0.5


    # Use Capital first letter (custom or prexisting class)

# Whenever you create a new point you instentiate the point class
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1.x,p1.y)
print(p1)
p3 = Point(4, 3)
print(p3.distance_origin())
p4 = Point(12, 5)
print(p4.distance_origin())
points = [p1, p2, p3, p4, Point(-2, 6)]
points.append(Point(-5,-5))
# You can append new points or just mannually add it in
print(points[4].x)
print(points[5].distance_origin())
# Entire list to be printed
print(points)
