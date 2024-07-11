num = int(input("input number :"))

def first():
    print("first")
    
    for i in range(0, num +1):
        print("*" * i)
        
    print("-------------------")
    
def  second():
    print("second")   
    
    for i in range(num, 0, -1):
        print("*" * i)
        
    print("-------------------")
    
def third():
    print("third")
    
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        print("* " * i)
        
    print("-------------------")

def fourth():
    print("fourth")
    
    for i in range(num):    
        print(" " * i , end = "")
        print("* " * (num - i ))
        
    print("-------------------")

def fifth():
    print("fifth")
    
    for i in range(1, num + 1):
        print(" " * (num - i), end="")
        print("*" * i)



    
first()
second()
third()
fourth()
fifth()