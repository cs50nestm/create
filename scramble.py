from cs50 import get_string
import random

def main():
    # Open text file with words
    file = open("word_list.txt")

    # Create a list from the text file
    # THIS SHOWS DATA BEING STORED IN A LIST
    word_list = file.readlines()

    # Genererate a random index to choose random word
    index = random.randint(0, len(word_list) - 1)

    # Strip of the \n character at the end of the selected word
    # THIS SHOWS THE LIST BEING USED
    word = word_list[index].rstrip("\n")

    # Get a list of scrambled letters in word
    scrambled_list = scramble_word(word)

    # Create a string from the list of chars with spaces in between
    separator = ' '
    print(f"Your scrambled word is: {separator.join(scrambled_list)}")

    # Loop to give user multiple chances to guess the scrambled word
    while True:
        guess = get_string("Guess: ")

        # If user doesn't enter anything at prompt, they are done!
        if not guess:
            print("Too bad you are giving up!")
            break

        # Congratulate user when they correctly guess word
        if check_word(guess, word):
            print("Congrats!")
            break


# Create a list from word to shuffle letters
def scramble_word(word):
    # THIS IS ANOTHER EXAMPLE OF DATA (characters) BEING STORED IN A LIST
    word_list = list(word)

    # THIS IS ANOTHER EXAMPLE OF A LIST BEING USED
    random.shuffle(word_list)
    return word_list


# Check if guess is correct
# THIS FUNCTION HAS TWO PARAMETERS (guess and word)
def check_word(guess, word):

    # First check if lengths of the guess and the random word match
    # THIS IS SELECTION
    if len(guess) != len(word):
        # THIS SEGMENT EXECUTES IF LENGTHS ARE DIFFERENT
        print("Wrong number of characters!")
        return False

    # Then check character by character for wrong letter
    # THIS IS ITERATION
    # THIS SEGMENT EXECUTES IF LENGTHS ARE THE SAME
    for i in range(len(guess)):
        if guess[i] != word[i]:
            print("Sorry not there yet!")
            print(f"Hint: Your first {i} characters are correct!")
            return False

    # Since we didn't return above guess is correct!
    return True


main()