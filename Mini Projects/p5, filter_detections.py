def filter_detections(detections, min_confidence=0.5):
    valid_detections = []
    
    for item in detections:
        if item["confidence"] >= min_confidence:
            valid_detections.append(item)
            
    return valid_detections


def display_report(filtered_data):
    print("--- Detected Objects Report ---")
    for item in filtered_data:
        label = item["label"]
        conf_percent = int(item["confidence"] * 100)
        print(f"{label:<15} -> Confidence: {conf_percent}%")


raw_data = [
    {"label": "car", "confidence": 0.85},
    {"label": "person", "confidence": 0.42},
    {"label": "truck", "confidence": 0.78},
    {"label": "traffic_light", "confidence": 0.35}
]

filtered = filter_detections(raw_data, min_confidence=0.5)

display_report(filtered)
