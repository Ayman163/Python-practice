speed_limit = int(input("Enter the speed limit: "))
driver_speed = int(input("Enter the driver speed: "))

if driver_speed <= speed_limit:
    print("Speed is safe. Have a good trip!")
elif driver_speed > speed_limit:
    over_limit = driver_speed - speed_limit
    if over_limit > 0 and over_limit <= 20:
        print("You are over the speed limit by", over_limit, "km/h.\nFine is $50")
    elif over_limit > 20 and over_limit <= 40:
        print("You are over the speed limit by", over_limit, "km/h.\nFine: $150")
    elif over_limit > 40:
        print("You are over the speed limit by", over_limit, "km/h.\nFine: $300 + License Suspended!")
