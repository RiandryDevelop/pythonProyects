import random


def guessNumber(x):
    chances = 3
    random_number = random.randint(1,  x)
    number_toguess = 0

    while number_toguess != random_number and chances == 0:
        chances -= 1
        print("You got :", chances)
        print(f"Guess a number between 1 to {random_number}")
        number_toguess = int(input("Guess the number:"))

        if number_toguess < random_number:
            print(f"Sorry, guess again , the number is greater than {number_toguess}")

        elif number_toguess > random_number:
            print(f"Sorry, guess again , the number is less than {number_toguess}")

        else:
            print(f"Sorry , this( {number_toguess}) is not the number, Try again:\n")
            continue


    print(f" {random_number} =  {number_toguess}")
    print(f"You've guessed the number ({random_number}) , Congratulations!!!")



guessNumber(11)
