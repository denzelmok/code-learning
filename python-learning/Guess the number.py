# Randomly generate a number between 0 and 20. User needs to guess what number is
# If user guesses wrong, tell them guess is either too high, or too low


def user_guess():
    import random
    random = random.randint(0, 20)
    print("Guess the number!")
    guess = int(input("Your guess: "))
    print()

    while guess != random:
        print("You have guessed wrong!")
        if guess > random:
            print("Your number is too high!")
            print("Guess again!")
            guess = int(input("Your guess: "))
            print()
        if guess < random:
            print("Your number is too low!")
            print("Guess again!")
            guess = int(input("Your guess: "))
            print()
        if guess == random:
            break

    print("Congratulations, you have guessed correctly!")
    print("Try again? Please type in Y or N")

    again = input()
    if again in ["N", "n"]:
        print("Game is exiting")

    if again in ["Y", "y"]:
        user_guess()


user_guess()
