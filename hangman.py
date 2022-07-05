## HANGMAN GAME
import random
from pyparsing import alphas
from helpers import draw

# keep a track of guessed letters
guessed = set()

# generate word 
words = open("words.txt", "r")
wordList = words.read().split(", ")
word = random.choice(wordList).upper()

# keep track of letters in word
letters = set()
for letter in word:
    letters.add(letter)

# print a dash for each letter in word
print("\n")
for letter in word:
    print("_", end="")
print("\n")

def hangman():

    lives = 7
    while lives > 0:

        draw(lives)

        if letters.issubset(guessed):
            print("You win!!")
            return 0

        print(f"You have {lives} lives left.")
        if guessed:
            print("You have guessed: ", guessed)
        guess = input("Guess a letter: " ).upper()
        
        print("\n")

        if guess not in alphas:
            print(f"{guess} is not a letter.")

        elif guess not in guessed:
            guessed.add(guess)
            if guess not in word:
                lives -= 1
        
        else: 
            print(f"You have already guessed {guess}.")

        for letter in word:
                if letter in guessed:
                    print(letter, end="")
                else:    
                    print("_", end="")
        print("\n")

    draw(lives)
    print(f"YOU LOSE!! The word was {word.lower()}")

hangman()
# if incorrect, store letter somewhere

