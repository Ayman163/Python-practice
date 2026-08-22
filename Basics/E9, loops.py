print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

secret_code = "ai2026"
attempts = 0

while attempts < 3:
    user_attempt = input("Enter access code: ")
    if user_attempt == secret_code:
        print("Access Granted!")
        break
    attempts += 1
    print(f"Wrong code. Attempts remaining: {3 - attempts}")
else:
    print("Account locked due to too many failed attempts.")

print("Printing only odd numbers:")
for num in range(1, 10):
    if num % 2 == 0:
        continue 
    print(num)
