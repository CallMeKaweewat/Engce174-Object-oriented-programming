# Dictionary of lists: Mapping cities to their temperature
cities = {
    'New york': [32, 25, 30, 28, 35],
    'Los angeles': [75, 68 ,72 ,70 ,80],
    "chicago": [20, 18, 22, 25, 15]
}

#calculate average temperature for each city
average = {city: sum(temps) / len(temps) for city, temps in cities.items()}
print("Avarage temeratures:", average)
#output: {'New york': 30.0, 'Los angeles': 73.0, 'chicago': 20.0}