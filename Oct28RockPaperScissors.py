import random

def menuOptions():

    choice = 0


    while choice == 0:

        print("1) New Game")
        print("2) Exit")
        choice = int(input("Select a menu option: "))

        if choice > 2:
            choice = 0
        elif choice == 1:
            ComputerChoice()
        else:
            print("Goodbye")

    return choice

def ComputerChoice():

    random_value = random.randint(1,3)

    if random_value == 1:
        computer_select = "rock"
    elif random_value == 2:
        computer_select = "paper"
    else:
        computer_select = "scissors"

    return computer_select


def UserChoice():

    user_value = 0

    while user_value == 0:

        print("1) rock")
        print("2) paper")
        print("3) scissors")
        user_value = int(input("Choose your weapon: "))

        if user_value == 1:
            user_select = "rock"
        elif user_value == 2:
            user_select = "paper"
        elif user_value == 3:
            user_select = "scissors"
        else:
            user_value = 0

    return user_select

def game(user_select, computer_select):
    pass

## TRY FILLING OUT THIS FUNCTION AND THEN RUNNING A GAME