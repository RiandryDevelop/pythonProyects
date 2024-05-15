# # We're gonna make a rock,paper,scissors game
# import random
#
# user_wins = 0
# computer_wins = 0
# options = ["rock", "paper", "scissors"]
#
#
# while True:
#     random_options = random.randrange(3)
#     print("Computer Wins: ", computer_wins)
#     print("User Wins: ", user_wins)
#
#     user_answer = input("Type Rock, Paper, Scissors Or Q to quit the game:\n ").lower()
#     if user_answer == "q":
#         break
#     if user_answer not in options:
#         continue
#
# # this work if you both are tied
#     if user_answer == options[random_options]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("you're both  tied")
#
#     if user_answer == 'rock' and options[random_options] == options[1]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("You LOSE !!!")
#         computer_wins += 1
#     if user_answer == 'rock' and options[random_options] == options[2]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("You WON")
#         user_wins += 1
#
#     if user_answer == 'paper' and options[random_options] == options[0]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("You WON")
#         user_wins += 1
#
#     if user_answer == 'paper' and options[random_options] == options[2]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("You LOSE")
#         computer_wins += 1
#
#     if user_answer == 'scissors' and options[random_options] == options[0]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("You LOSE")
#         computer_wins += 1
#
#     if user_answer == 'scissors' and options[random_options] == options[1]:
#         print("Your answer was: ", user_answer)
#         print("Computer answer was: ", options[random_options])
#         print("You WON")
#         user_wins += 1
#


#
# print("GOOD BYE !!!")

from collections import Counter
def most_common_letter(input_string):
    # count the repetition of the letters
    letter_count = dict(Counter(input_string))

    # count(value) of the most common letter/s
    max_count = max(letter_count.values())

    # list of most common letter/s
    most_common = [key for key in letter_count if letter_count[key] == max_count]

    return f"Repetitions of the letters: {letter_count} \n" \
           f"The Maximum letter counted: {max_count} \n" \
           f"Most common letter: {most_common}"

print(most_common_letter("HHHKKIOPSWB"))
