# Tuple initialization
coordinates = (3, 5)

# Unpacking tuples
x ,y = coordinates
print("x-coordinate", x)        #output 3
print("y- coordinate", y)       #output 5

#tuple as keys in dictionary
location = {(3, 5): "Home", (10, 20): "office"}
print("Location at (3,5):", location[(3, 5)])       #output Home