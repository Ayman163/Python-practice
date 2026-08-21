score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

passport = True
age = int(input("Enter your age: "))
if age < 18:
    passport = False
    print("Sorry, you are not eligible for a passport.")
elif age >= 18:
    print("You are eligible for a passport.")
