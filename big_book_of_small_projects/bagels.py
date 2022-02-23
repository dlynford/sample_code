# 2/22/2022
import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"""Bagels, a deductive logic game. 
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS} digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct and in the right position.
    Bagels      No digit is correct.
    """)

    while True: #main game loop.
        #This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # Keep looping until they enter a vaild guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess #{numGuesses}: ")
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break #they're correct so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('you ran out of guesses.')
                print(f"The answer was {secretNum}.")

        # Ask player if they want to play again?
        print("Do you want to play again? (yes or no)")
        if not input('> ').lower().startswith('y'):
            break
    print("Thanks for playing!")

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') #create a list of digits 0 to 9.
    random.shuffle(numbers) # shuffle them into random order.

    # get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return "You got it!"
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico')
    if len(clues) == 0:
        # There are no correct digits at all.
        return 'Bagels'
    else:
        # Sort the clues into alphabetical order so their original order doesn't give away information.
        clues.sort()
        # make a single string from the list of clues.
        return" ".join(clues)

# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
