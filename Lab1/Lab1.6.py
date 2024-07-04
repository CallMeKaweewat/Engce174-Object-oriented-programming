names = ["alice","bob","charlie"]
age = [25,30,35]
city = ["New yoke", "Los angeles", "chicago"]

#Using zip() for parallel iteration
for names, age, city in zip(names, age, city):
    print(f"{names} is {age} year old and live in {city}")

#output
#alice in 25 years old and live in newyoke
#bob is 30 years old and live in los angeles
#charlie is 35 years old and live in chicago
    