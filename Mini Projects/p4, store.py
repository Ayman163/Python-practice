inventory = {"Arduino": 10, "Sensor": 3, "Camera": 8}

while True:
    print("-" * 50)
    print("Select your choice:")
    print("1. Show all products")
    print("2. Add / Update product")
    print("3. Scan low stock products (< 5)")
    print("4. Exit")
    print("-" * 50)
    
    inputt = int(input("Enter choice: "))

    if inputt == 1:
        print("\n--- Current Inventory ---")
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")
            
    elif inputt == 2:
        product_name = input("Enter product name: ")
        quantity_ = int(input("Enter quantity: "))
        
        if product_name in inventory:
            inventory[product_name] += quantity_
            print(f"Updated {product_name} total: {inventory[product_name]}")
        else:
            inventory[product_name] = quantity_
            print(f"Added new product: {product_name}")

    elif inputt == 3:
        print("\n--- Low Stock Alert (< 5) ---")
        found_low = False
        for product, quantity in inventory.items():
            if quantity < 5:
                print(f"Warning: {product} has only {quantity} left!")
                found_low = True
        if not found_low:
            print("All items have sufficient stock.")

    elif inputt == 4:
        print("Exiting Inventory Manager. Goodbye!")
        break
    else:
        print("Invalid choice, please select between 1 and 4.")
