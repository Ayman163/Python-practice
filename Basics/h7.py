detections = [
    ("car", (10, 20, 110, 120)),
    ("person", (50, 50, 70, 90)),
    ("truck", (0, 0, 200, 150)),
    ("traffic_sign", (30, 40, 45, 55))
]

filtered_detections = [
    {"label": label, "area": (x2 - x1) * (y2 - y1)}
    for label, (x1, y1, x2, y2) in detections
    if (x2 - x1) * (y2 - y1) >= 1000
]

print(filtered_detections)
