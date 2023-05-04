import random
import string
from wordsList import wordsList

life = 7

hangmanBoard = [['_', '_', '_', ' ', ' '],
['|', ' ', '|', ' ', ' '],
['|' , ' ', ' ', ' ', ' '],
['|' , ' ', ' ', ' ', ' '],
['|' , ' ', ' ', ' ', ' '],
['-' , '_', '_', ' ', ' ']]

bank = ['_', '_', '_', '_', '_']

alphabet = set(string.ascii_lowercase)

guessed = []

#Choose a word
def chooseWord():
    x = random.randint(0, len(wordsList))
    Chosen = wordsList[x]
    return Chosen

chosenW = chooseWord()

#Print Score
def score():
    print("Bank: ", *bank, "\n", "Guessed Characters: ", guessed, "\n", "Lives Remaining: ", life)

#Print the Board
def printboard():
    for i in hangmanBoard:
        print('{} {} {} {} {}'.format(*i, sep = ' '))

#print game and score
def game(life):
    getHangmanBoard(life)
    printboard()
    score()

#replace list with body
def getHangmanBoard(life):
    match life:
        case 6:
            hangmanBoard[2][2] = "O"
        case 5:
            hangmanBoard[3][2] = "|"
        case 4:
            hangmanBoard[3][1] = "/"
        case 3:
            hangmanBoard[3][3] = "\\"
        case 2:
            hangmanBoard[4][1] = "/"
        case 1:
             hangmanBoard[4][3] = "\\"

#contains character
def containsCharacter(char):
    for i in range(0, len(chosenW)):
        if chosenW[i] == char:
            bank[i] = char

#game
while life > 0 or "_" not in bank:
    game(life)
    uInput = input("Please put in your guess: ").lower()
    if (not len(uInput) == 1) or uInput not in alphabet or uInput in guessed:
        print("Please put in a valid letter!")
    else:
        if uInput in chosenW:
            containsCharacter(uInput)
            guessed.append(uInput)
        else:
            life = life - 1
            guessed.append(uInput)

if life == 0:
    print("You ran out of lives!")
    print("The word was " + chosenW + "!")
else:
    print("You won!")
