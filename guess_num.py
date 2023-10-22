import random

def guess_num():

    to_be_guessed = random.randint(1, 100)

    while True:

        try:
            player_input = int(input("Guess my number (1-100): "))
            if player_input == to_be_guessed:
                print("Congratulations, you guessed!")
                break
            elif 1<=player_input < to_be_guessed:
                print("Higher")
            elif 100>=player_input > to_be_guessed:
                print("Lower")
            else:
                print(f"{player_input} isn't a number between 1 and 100")

        except ValueError:
            print("Only integers allowed")

guess_num()

while True:

    try:
        continue_game = input("Would you like to continue? (Y/N)\n")
        if continue_game=="Y":
            guess_num()
        elif continue_game=="N":
            print("Maybe you'd like to check out my other projects on https://github.com/NikolaiKrustev03")
            break
        elif not continue_game.isalpha():
            print(f"{continue_game} not allowed. Only Y or N as a valid answer")
        else:
            print("Only Y or N as a valid answer")

    except ValueError:
        print("Invalid answer")
