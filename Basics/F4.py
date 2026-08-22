name = input("What is your name? ")
reversed_text = ""
vowels_count = 0

for char in name:

    reversed_text = char + reversed_text
    
    if char.lower() in "aeiou":
        vowels_count += 1

print(f"Reversed text: {reversed_text}")
print(f"Vowels count: {vowels_count}")
