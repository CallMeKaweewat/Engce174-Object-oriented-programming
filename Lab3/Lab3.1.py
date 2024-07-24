x = int(input('Enter your number: '))

def first(n):
    for i in range(0, n):
        for j in range(0, i+1):
            print('*', end=" ")
        print("")

def seccond(n):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print('*', end=" ")
        print("")

def third(n):
    for i in range(n):
        print(" "*(n-i-1), end="")
        for j in range(i+1):
            print('*', end=" ")
        print("")

def fourth(n):
    for i in range(n, 0, -1):
        print(" "*(n-i), end="")
        for j in range(i):
            print('*', end=" ")
        print("")

def fifth(n):
    for i in range(n):
        for j in range(i, n):
            print(' ', end=" ")
        for j in range(i+1):
            print('*', end=" ")
        print("")

def result(number):
    numpat_ = first(number)
    print("-------------------------")
    
    numpat_rotate = seccond(number)
    print("-------------------------")
    
    pyramid_ = third(number)
    print("-------------------------")
    
    pyramid_rotate = fourth(number)
    print("-------------------------")
    
    numpatright_ = fifth(number)
    print("-------------------------")
    
    return numpat_, numpat_rotate, pyramid_, pyramid_rotate, numpatright_

numpat_, numpat_rotate, pyramid_, pyramid_rotate, numpatright_ = result(x)