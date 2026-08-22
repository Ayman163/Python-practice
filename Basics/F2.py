number = int(input("Enter a number: "))
total = 0

if number > 0:
    for i in range(1, number + 1):
        total += i
    print(F"The sum of the numbers from 1 to {number} is {total}")
else:
    print("Please enter a positive number")
