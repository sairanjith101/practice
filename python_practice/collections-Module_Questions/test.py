from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10,12)
print(p.y)
