inventory = {"Arduino": 10, "Sensor": 3, "Camera": 8}

while True:
    print("-"*50)
    print("select your choice:")
    print("1.show all product")
    print("2.add product")
    print("3.scan all product")
    print("4.exit")
    inputt = int(input(":"))
    if inputt == 1:
        print("-"*50)
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")
            
    elif inputt == 2:
        product_name = input("Enter the name of product:")
        quantity_ = int(input("Enter the number of product:"))
        for product, quantity in inventory.items():
            if product_name == product:
                inventory[product] += quantity
            elif product_name != product:
                inventory[product_name] = quantity_
            else:
                print("you write somethink wrong")
    elif inputt == 3:
        for product, quantity in inventory.items():
            if quantity < 5:
                print(f"{product}: {quantity}")
            else:
                continue
    elif inputt == 4:
        break
    else:
        print("Invalid task number.")
