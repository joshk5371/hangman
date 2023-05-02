import random
import re
from wordsList import wordsList

# Create hangman board
hangmanBoard = [
''' +---+
     |
     |
     |
    ===''', '''
 +---+
 O   |
     |
     |
    ===''', '''
 +---+
 O   |
 |   |
     |
    ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
 O   |
/|\  |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''']

life = 6

guessedCharacters = []

def chooseWord():   
    x = random.randint(0, len(wordsList) - 1)
    word = wordsList[x]
    return word

def printHangman(life):
    print(getHangmanBoard(life))
    print("Word: " , current)
    print("Guessed Character: ", guessedCharacters)
    print("Amount of guesses left: " , life)

def getHangmanBoard(life):
    match life:
        case 6:
            return hangmanBoard[0]
        case 5:
            return hangmanBoard[1]
        case 4:
            return hangmanBoard[2]
        case 3:
            return hangmanBoard[3]
        case 2:
            return hangmanBoard[4]
        case 1:
            return hangmanBoard[5]
        case _:
            return hangmanBoard[6]

def containsCharacter(char):
    for i in range(0, len(chosenWord)):
        if chosenWord[i] == char:
            current[i] = char


# Get a random word from the list

chosenWord = chooseWord()

# Let the player know how many letters are in the word (Ex: _ _ _ _ _ ) (Make an array of characters)
## The length will always be 5

current = ['_','_','_','_','_']    

# Let the player guess a letter (need edge cases for this (answer must be a-z, must be length one, cannot be blank, cannot be a character that was already guessed etc))
while life > 0 or "_" not in current:
    printHangman(life)
    user_input = input("Please type in a letter: ").lower()
    if (not (len(user_input) == 1 and re.match('[a-z]', user_input))) or user_input in guessedCharacters:
        print("Please enter a valid letter!")
    else:
        # If the word contains the letter, add the letter to the array of characters
        # If the array of characters no longer has any missing characters, player wins
        if user_input in chosenWord:
            containsCharacter(user_input)
        # If it doesn't, add a body part to the hangman board (maybe create a counter for each wrong guess) (Let the user know which characters they've already guessed)
        else: 
            print("This character is not in the word!")
            life = life - 1
            guessedCharacters.append(user_input)
printHangman(life)
if life == 0:
    print("You lost loser!")
    print("The word was " + chosenWord + "!")
else:
    print("You won!")


