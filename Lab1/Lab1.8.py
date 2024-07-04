from collections import namedtuple

# Define a named tuple
Point = namedtuple('Point', ['X', 'Y'])

# Create instances of the named tuple
p1 = Point(3, 5)
p2 = Point(-1, 2)

# Access element by name
print("Coordinates of p1:", p1.X, p1.Y)      #output 3 5