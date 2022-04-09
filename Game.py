import random

# Get a random number from 0 to 100
rand_number = random.randint(0,101)

def guessingGame(player_guessed_numb:int, tries_left: int, number_tries:int):
    """
    The guessing game: Player try to guess the number randomly generated by the computer

    Input Parameter
    ***************
    player_guessed_numb: An integer number from 0 to 100

    Output
    ******
    The game indicate if you guessed right or wrong.

    Example
    *******
    Please guess a number between 0 to 100 : 56

    >>>You guessed Right
    >>>It took you 4 guesses
    >>>The correct answer is 56

    """
 
    if player_guessed_numb == rand_number:
        print("\nYou guessed Right")
        print(f"It took you {number_tries} guesses")
        print(f"The correct answer is {rand_number}")
    elif player_guessed_numb > rand_number:
        print("\nWrong : You guessed too high")
        if tries_left != 0 : print("Try again!!!")
        print(f"You have {tries_left} tries left")
    elif player_guessed_numb < rand_number:
        print("\nWrong: You guessed too low")
        if tries_left != 0 : print("Try again!!!")
        print(f"You have {tries_left} tries left")


#Get guessed number from player
max_tries = 6
tries_leftn = max_tries
number_triesn=0


while number_triesn < max_tries:
    try:
        player_number = int(input("\nPlease guess a number between 0 to 100 : "))
        tries_leftn = tries_leftn - 1
        number_triesn = number_triesn + 1
        guessingGame(player_number,tries_leftn,number_triesn)

        if player_number == rand_number:
            break
    except ValueError as err:
        print("\nPlease enter a valid number :", err)
else:
    print(f"\nYou have reached your maximum tries {max_tries}")
    print(f"The correct answer is {rand_number}\nGame Over!!!")


