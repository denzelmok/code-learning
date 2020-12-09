# rock paper scissors game with player against computer
# computers answer is randomly generated
# program will ask user for input

import random

options = ['Rock', 'Paper', 'Scissors']


def game_start():
    print("Type in rock, paper or scissors!")
    user_choice = input("Your choice: ").capitalize()
    comp_choice = random.choice(options)
    print("The computer has chosen: " + comp_choice)

    # find position of choice in list
    user_index = options.index(user_choice)
    comp_index = options.index(comp_choice)

    if user_index < comp_index and user_index != comp_index and user_index != 2:
        print("You lose!")

    if user_index > comp_index != 2 and user_index != comp_index:
        print("You win!")

    if user_index == comp_index:
        print("It is a draw!")

    if user_index == 3:
        print("Play again!")

    game_start()


game_start()
