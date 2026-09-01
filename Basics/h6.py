raw_labels = ["  car ", "PERSON", " truck", "BICYCLE ", "bus", "  TRAIN  "]
labels = [x.strip().lower() for x in raw_labels if len(x.strip()) >= 4]
print(labels)
