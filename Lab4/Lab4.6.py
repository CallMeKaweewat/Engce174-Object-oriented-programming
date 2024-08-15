# Given a list of numbers, remove all occurrences of a specific number and calculate the sum of remaining numbers.

# List number
numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]
remove_num = 3

# remove number
while remove_num in numbers:
    numbers.remove(remove_num)

# show result remove number
print("Numbers after removal:", numbers) # result: Numbers after removal: [1, 2, 4, 5, 6, 7]

#  calculator total of number
print("Sum of remaining numbers:", sum(numbers)) # result: Sum of remaining numbers: 25