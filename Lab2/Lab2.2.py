num = int(input("input number: "))

def first(i = 0):
    if i > num:
        return
    print('*' * i)
    first(i + 1)

def second(i = num):
    if i == 0:
        return
    print('*' * i)
    second(i - 1)

def third(i = 1):
    if i > num:
        return
    print(' ' * (num - i) + '* ' * i)
    third(i + 1)

def fourth(i = num):
    if i == 0:
        return
    print(' ' * (num - i) + '* ' * i)
    fourth(i - 1)

def fifth(i = 1):
    if i > num:
        return
    print(' ' * (num - i) + '*' * i)
    fifth(i + 1)

print("first")
first()
print("-------------------")

print("second")
second()
print("-------------------")

print("third")
third()
print("-------------------")

print("fourth")
fourth()
print("-------------------")

print("fifth")
fifth()
