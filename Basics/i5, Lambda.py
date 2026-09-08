speeds = [115, 140, 95, 130, 110]

violators = list(filter(lambda s: s > 120, speeds))

print(violators)
