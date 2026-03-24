from session_1 import Point

class ColorPoint(Point):
    def __init__(self,x,y,color):
        if not isinstance(x,(int,float)):
            raise TypeError
        if not isinstance (y,(int,float)):
            raise TypeError
        self.x = x
        self.y = y
        self.color = color
    def __str__(self):
        # We over-write the __str__ from the parent
        return f"{self.color}: cp<{self.x},{self.y}>"

if __name__=="__main__":
    p1 = ColorPoint(1,2, "red")
    p2 = ColorPoint(2,3, "blue")

    print(p1.x, p1.y, p1.color)
    print(p2)
    p3=Point(1, 2)
    # Because I have not touched the def in here, it calls the parent method.
    print(p2.distance_origin())
    points = [p1, p2, p3]
    print(points)

    points.append(Point(2,0))
    points.append(-1)
    points.sort()
    print(points)

    p5=ColorPoint(p1, p2, "red")
    print(p5)