model_info = {
    "name" : "YOLOv8",
    "task" : "Object Detection",
    "accuracy" : 0.89,
    "classses" : ["car", "person", "truck"]
}

print(model_info["name"])
print(model_info.get("speed","Unknown"))
print(model_info)

print("-"*50)

for key, value in model_info.items():
    print(f"{key}: {value}")
