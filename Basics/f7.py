data = [12, -7, 5, -3, 12, 8, -7, 20, 5]
positive_unique = []

for i in data:
    if i > 0 and i not in positive_unique:
        positive_unique.append(i)

print(positive_unique)
