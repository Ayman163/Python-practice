cars = [
    {"brand": "Toyota", "speed": 130},
    {"brand": "Tesla", "speed": 145},
    {"brand": "Nissan", "speed": 125},
    {"brand": "BMW", "speed": 160}
]

sorted_cars = sorted(cars, key=lambda car: car["speed"])

print(sorted_cars)
