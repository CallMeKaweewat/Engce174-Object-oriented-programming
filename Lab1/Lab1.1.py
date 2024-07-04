#List comprehension
squaes = [X**2 for X in range(10)]      #create list number of exponent (2)
#Dictionary comprehension
square_dict = {X: X**2 for X in range(5)}   #create dictionary key 0-4 and value exponent (2)
#Set comprehension
even_squares = {X**2 for X in range(10) if X % 2 == 0}  #creat set values exponent (2) 0-9 dicide by 2

print("sq = "   ,squaes)
print("sq_dict = " ,square_dict)
print("even_sq = " ,even_squares)