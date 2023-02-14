import random
to_be_guessed=random.randint(1,100)
passing=False
while True:
    try:
        player_input=int(input("Guess my number (1-100): "))
        if player_input==to_be_guessed:
            print("Congratulations, you guessed!")
            break
        elif player_input<to_be_guessed:
            print("Higher")
        elif player_input>to_be_guessed:
            print("Lower")
    except ValueError:
        print("Only integers allowed")