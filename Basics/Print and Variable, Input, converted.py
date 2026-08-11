# 1. Variable Assignment and Printing
user_name = "Ayman"  # str (String / سلسلة نصية)
age = 22             # int (Integer / عدد صحيح)
gpa = 3.85           # float (Float / عدد عشري)
is_student = True    # bool (Boolean / قيمة منطقية)

# 2. String Formatting (f-strings)
print(f"Developer: {user_name}, Age: {age}, GPA: {gpa}")

# 3. Reading Input from User
# Note: input() always returns a string (str)!
user_input_age = input("Enter your age: ")
converted_age = int(user_input_age)  # Typecasting (تحويل النوع)

print(f"Next year you will be {converted_age + 1} years old.")
