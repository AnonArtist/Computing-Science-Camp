import random
import sys

wordlist = ["awkward", "bagpipes", "croquet", "crypt", "dwarf", "fishhook", "gypsy", "oxygen", "pixel", "zombie"]
guess_word = []
secretWord = random.choice(wordlist)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []

def beginning():
    print("Hello. Welcome to Hangman. Try your best to spell out the secret word.")
    while True:
        name = input("Please enter your name. ")
        if name == '':
            print("You cannot do that. Please enter your name. ")
        else:
            break
    
beginning()
    
def newFunc():
    print("Now that you have entered a name, let's begin!")

newFunc()

def change():
    for character in secretWord:
        guess_word.append("-")

print("The word you need to guess has", length_word, "characters")
print("You can only enter letters from A to Z.")
print(guess_word)

def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input
        guess = input("Pick a letter ").lower()
        if not guess in alphabet:
            print("Please enter a letter from A to Z.")
        elif guess in letter_storage:
            print("You have already guessed that letter.")
        else:
            letter_storage.append(guess)
            if guess in secretWord:
                print("That was correct!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)
                        
                        if not '-' in guess_word:
                                           print("You won!")
                                           break

    else:
        print("Sorry, that was not correct. Try again.")
        guess_taken += 1
        if guess_taken == 10:
            print(" Sorry, you lost. The secret word was", secretWord)
        
change()
guessing()
print("Game over.")