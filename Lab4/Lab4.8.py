# create number 1 to 10
even_numbers = {x for x in range(1, 11) if x % 2 == 0}

print("Even numbers:", even_numbers) # result: Even numbers: {2, 4, 6, 8, 10}