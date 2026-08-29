def calculate_area(width, height):
    area = width * height
    return area

room_area = calculate_area(5, 4)
print(f"Room area: {room_area}")

def greet_user(name, title="Student"):
    return f"welcome, {title} {name}"

print(greet_user("Ayman"))
print(greet_user("Ayman", title="Eng."))
