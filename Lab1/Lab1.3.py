def fibonacci():        #using fibo to enter number start at a, b 1, 2
    a, b = 0, 1
    while True:
        yield a         # return a and stop working untill call next()
        a, b = b, a + b     # update a and b to b and a+b for create value fibo
        
fib = fibonacci()
print(next(fib))        #output 0
print(next(fib))        #output 1
