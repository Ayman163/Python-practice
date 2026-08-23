speed_limit = int(input("Enter the speed limit: "))
driver_speed = int(input("Enter the driver speed: "))

if driver_speed <= speed_limit:
    print("Speed is safe. Have a good trip!")
else:
    over_limit = driver_speed - speed_limit
    if over_limit <= 20:
        
        print(f"You are over the speed limit by {over_limit} km/h.\nFine is $50")
    elif over_limit <= 40:
        
        print(f"You are over the speed limit by {over_limit} km/h.\nFine: $150")
    else:
        
        print(f"You are over the speed limit by {over_limit} km/h.\nFine: $300 + License Suspended!")
