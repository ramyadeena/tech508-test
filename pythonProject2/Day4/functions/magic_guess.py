

magic_number = 43
guess_left = 5

while guess_left > 0:
    guess = int(input("Enter the guess: "))

    if guess == magic_number:
        print("you won")
        break
    elif guess > magic_number:
        print("Guess lower")
    elif guess < magic_number:
        print("Guess higher")
    guess_left -= 1
    print(f"you have {guess_left}  guesses left")

    if guess_left ==0:
        print("no more guesses . better luck next time")
        print(f"The magic number is {magic_number}")


# import random  # this will generate a random number for user to guess
#
# number = random.randint(1,20)
# guess = 0
#
# while guess != number:
#     guess = int(input("enter guess: "))
#     if guess > number:
#         print("guess lower")
#     elif guess < number:
#         print("guess higher")
#     else:
#         print("you won")

