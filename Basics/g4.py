search_keywords = ["python", "ai", "python", "fastapi", "ai", "yolo", "python", "ai"]

unique_keywords = set(search_keywords)
print(f"Unique Keywords: {unique_keywords}")

word_counts = {}

for word in search_keywords:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print("\n--- Keyword Frequency Report ---")
for word, count in word_counts.items():
    print(f"{word}: {count} times")
