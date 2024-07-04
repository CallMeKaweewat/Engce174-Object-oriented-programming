# Dictionary initialaztion
person = {'name': 'Alice', 'age': 30, 'city': 'New york' }  # Key ,values

#accessing values
print("Name:", person['name'])      #output alice

#updateing values
person['age'] = 31
print("updated age:" , person['age'])       #output 31

#iterating thriygh keys and values
for key, value in person.items():
    print(f"{key}: {value}")

#Output: 
#Name alice
#Age 31
#city newyork
