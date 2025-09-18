import random
number_to_guess = random.randint(1,100)
attempts = 0
while True:
    try:
        guess = int(input("Guess the number between 1 to 100: "))
        attempts += 1
        if guess > number_to_guess:
            print("Number too high choose another number...")
        elif guess < number_to_guess:
            print("Number too low chose another number...")
        else:
            print(f"Congratulations, You won in {attempts} attempts")
    except ValueError:
        print("Please enter a valid number...")