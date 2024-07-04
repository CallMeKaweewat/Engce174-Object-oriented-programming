#dictionary comprehension to create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares_dict = {num: num**2 for num in numbers}
print("Dictionary of squares:", squares_dict)

#output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}