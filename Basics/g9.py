def analyze_numbers(numbers: list):
    if not numbers:
        return None
    elif numbers:
        min_val = min(numbers)
        max_val = max(numbers)
        avg_val = sum(numbers) / len(numbers)

        return {"min": min_val, "max": max_val, "average": avg_val}

print(analyze_numbers([1,2,3,4,5,6,7,8,77]))
