import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from the list
    while '-' in word or ' ' in word:
        random.choice(words)

    return word.upper()

# function to keep track of which letters a user guesses and which 
# letters in the word they've correctly guessed
# It also keeps track of what is a valid letter and what isn't
def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphapet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (i.e W - R D) 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphapet - used_letters: # If user input is a valid letter in the alphabet that they haven't used before,
            used_letters.add(user_letter) # add the letter to the used_letters set
            if user_letter in word_letters: # If the letter a user guesses is in the word, remove the letter from word_letters
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters: # If letter entered by user is already in used_letters...
            print('You have already used that character. Please try again.')
        else: # If letter typed by a user is not in the alphabet and is not in used_letters
            print('Invalid character. Please try again')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("Congratulations! you guessed the word", word, "!!")

hangman()
# user_input = input('Type something: ')
# print(user_input)