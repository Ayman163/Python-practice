name = input("Enter your name: ")
target_specialty = input("Enter your target specialty: ")  
hours_per_week = int(input("Enter your hours per week available for study: "))
age = int(input("Enter your age: "))

monthly_hours = hours_per_week * 4

print("\n" + "=" * 35)
print("        USER PROFILE REPORT        ")
print("=" * 35)
print(f"Name             : {name}")
print(f"Age              : {age} years old")
print(f"Target Specialty : {target_specialty}")
print(f"Weekly Study     : {hours_per_week} hours")
print(f"Monthly Study    : {monthly_hours} hours/month")
print("=" * 35)
