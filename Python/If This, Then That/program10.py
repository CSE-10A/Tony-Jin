""""
WAP to guess a number between 1 and 9.

Note : User is prompted to enter a guess. If the user guesses wrong, then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
"""

import random
answer = random.randint(1, 9) # random number between 1 and 9
guess = 67 # set guess to number outside of range to start loop
while guess != answer: # loop until the guess is correct
    guess = int(input("Guess a number between 1 and 9: ")) # user input
print("Well guessed!") # correct guess message