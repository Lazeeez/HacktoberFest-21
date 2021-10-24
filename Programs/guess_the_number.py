# this module is used to generate the random no
import random

#here the random no is introduced to the program
random_no = random.randint(0, 1000)

while True:
    # using this variable, a guess will be taken and the number would then be compared
    no_guessed = int(input("Guess a number between 0 and 1000"))

    if no_guessed > random_no:
        print("Guess a smaller number")
        continue

    elif random_no > no_guessed:
        print("Guess a bigger number")
        continue

    else:
        print("you won")
        break
