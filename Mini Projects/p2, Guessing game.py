secret_number = 42
count = 0
while True:
    guess = input("Guess a number between 1 and 50: ")
    guess = int(guess)
    if guess > secret_number:
        print("Too high! Try a lower number.")
        print(F"You have {4 - count} guesses left.")
    elif guess < secret_number:
        print("Too low! Try a higher number.")
        print(F"You have {4 - count} guesses left.")
    else:
        print("You guessed the secret number!")
        break
    count += 1
    if count == 5:
        print("You lose!")
        break
