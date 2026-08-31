def calculate_discount(price, discount_percentage = 10):

    final_price = price - (price * discount_percentage / 100)

    return final_price

print(calculate_discount(int(input("Enter the price:")), int(input("Enter the discount:"))))
print(calculate_discount(int(input("Enter the price:"))))
