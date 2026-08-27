#raw is list 
raw_labels = ["car", "truck", "car", "bus", "person", "bus"]
#unqiue it's set
unique_labels = set(raw_labels)

print(unique_labels)  # {'car', 'truck', 'bus', 'person'}

#in set we use .add() not .append()
unique_labels.add("motorcycle")
