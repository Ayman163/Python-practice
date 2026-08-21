print("Welcome to my company!")
print("To complete your job application, please answer the following questions.")

name = input("What is your name? ")
age = input("What is your age? ")
gender = input("What is your gender? ")

years_of_experience = int(input("How many years of experience do you have? "))

knows_sql = input("Do you know SQL? ")

knows_git = input("Do you know Git? ")

if years_of_experience >= 5 and knows_sql == "Yes" and knows_git == "Yes":
    print("Your job title is:Senior Developer")

elif years_of_experience >= 2 and years_of_experience < 5 and (knows_sql == "Yes" or knows_git == "Yes"):
    print("Your job title is:Mid-level Developer")

elif years_of_experience < 2 and knows_sql == "Yes" and knows_git == "Yes":
    print("Your job title is:Junior Developer")

else:
    print("Sorry, you do not meet the minimum requirements.")

print("Thank you for your time.")
