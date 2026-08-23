print("Wlecome to my Calculator")

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

choice = input("Choose operation: +, -, *, /: ")

if choice == "+":
    print(number1 + number2)
elif choice == "-":
    print(number1 - number2)
elif choice == "*":
    print(number1 * number2) 
elif choice == "/":
    if number2 == 0: 
        print("Error: Division by zero is not allowed!")
    else:
        print(number1 / number2)
else:
    print("Invalid operation")
