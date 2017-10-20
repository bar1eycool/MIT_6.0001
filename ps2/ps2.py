# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    flag = 0
    
    for i in list(secret_word):
        if i in letters_guessed:
            flag += 1
    
    if (flag == len(secret_word)):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output_str = ''
    
    for i in list(secret_word):
        if i in letters_guessed:
            output_str += i
        else:
            output_str += '_ '
    
    return output_str


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    output_str = ''
    
    for alpha in list(string.ascii_lowercase):
        if alpha in letters_guessed:
            output_str += ''
        else:
            output_str += alpha
        
    return output_str

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    letters_guessed_list = [] # you can guess 6 times only
    letters_guessed_checklist = [] #for checking duplicate
    
    vowels_letters = ['a', 'e', 'i', 'o', 'u']
    
    guesses = 6
    warning = 3
    turns = 0
    score = 0

    print("Welcome to the game hangman!")
    print("I'm thinking of a word that is ", len(secret_word), " letters long")
    print("You have ", warning," warnings left.\n------------- ")
    print("You have ", (guesses - turns) ," guesses left.")
    
    print("Available letters:", get_available_letters(letters_guessed_list), end='')
    
    while (guesses > turns and (not is_word_guessed(secret_word, letters_guessed_list))):
        user_in = str.lower(input("Please guess a letter:"))
        letters_guessed_list += user_in
        
        
        if not (letters_guessed_list[turns] in list(string.ascii_lowercase)):
            if (warning <= 0):
                guesses -= 1
            else:
                warning -= 1
            print("Oops! That is not a valid letter. You have ", warning, " warnings left:", get_guessed_word(secret_word, letters_guessed_list))
            del letters_guessed_list[turns]
        elif (letters_guessed_list[turns] in letters_guessed_checklist):
            if (warning <= 0):
                guesses -= 1
            else:
                warning -= 1
            print("Oops! That is a duplicate letter. You have ", warning, " warnings left:", get_guessed_word(secret_word, letters_guessed_list))
            del letters_guessed_list[turns]
        elif (letters_guessed_list[turns] in secret_word):
            print("Good guess:", get_guessed_word(secret_word, letters_guessed_list))
            guesses += 1
            turns += 1
        else:
            if (letters_guessed_list[turns] in vowels_letters):
                print("Oops! Vowels letter is not in my word:", get_guessed_word(secret_word, letters_guessed_list))
                turns += 1
                guesses -= 1
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed_list))
                turns += 1
        
        print("------------- \nYou have ",(guesses - turns) ," guesses left.")
        print("Available letters:", get_available_letters(letters_guessed_list), end='')
        letters_guessed_checklist += user_in
    print("\n------------- ")
    turns -= 1
    
    score = (guesses - turns - 1) * len(set(secret_word))
    
    if (is_word_guessed(secret_word, letters_guessed_list)):
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was: ", secret_word)
    

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace("_ ", "_")
    correctness = 0    
    if (len(my_word) == len(other_word)):
        for i in range(len(my_word)):
            if (list(my_word)[i] == list(other_word)[i]):
                correctness += 1
            elif (list(my_word)[i] == '_'):
                if (other_word.count(list(other_word)[i]) > 1) and ((other_word)[i] in list(my_word)):
                    False
                else:
                    correctness += 1
            else:
                False
    else:
        return False
    
    if (correctness == len(other_word)):
        return True
    else:
        return False

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_list = ['',]
    del new_list[0]
    for count in range(len(wordlist)):
        if (match_with_gaps(my_word, wordlist[count])):
            new_list += [wordlist[count]]
    if (new_list == []):
        print('No matches found ')
    else:
        for x in range(len(new_list)):
            print(new_list[x], end= ' ')
        print(' ')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    
    letters_guessed_list = [] # you can guess 6 times only
    letters_guessed_checklist = [] #for checking duplicate
    
    vowels_letters = ['a', 'e', 'i', 'o', 'u']
    
    guesses = 6
    warning = 3
    turns = 0
    score = 0

    print("Welcome to the game hangman!")
    print("I'm thinking of a word that is ", len(secret_word), " letters long")
    print("You have ", warning," warnings left.\n------------- ")
    print("You have ", (guesses - turns) ," guesses left.")
    
    print("Available letters:", get_available_letters(letters_guessed_list), end='')
    
    while (guesses > turns and (not is_word_guessed(secret_word, letters_guessed_list))):
        user_in = str.lower(input("Please guess a letter:"))
        letters_guessed_list += user_in
        
        if (letters_guessed_list[turns] == '*'):
            show_possible_matches(get_guessed_word(secret_word, letters_guessed_list))
            del letters_guessed_list[turns]
        elif not (letters_guessed_list[turns] in list(string.ascii_lowercase)):
            if (warning <= 0):
                guesses -= 1
            else:
                warning -= 1
            print("Oops! That is not a valid letter. You have ", warning, " warnings left:", get_guessed_word(secret_word, letters_guessed_list))
            del letters_guessed_list[turns]
        elif (letters_guessed_list[turns] in letters_guessed_checklist):
            if (warning <= 0):
                guesses -= 1
            else:
                warning -= 1
            print("Oops! That is a duplicate letter. You have ", warning, " warnings left:", get_guessed_word(secret_word, letters_guessed_list))
            del letters_guessed_list[turns]
        elif (letters_guessed_list[turns] in secret_word):
            print("Good guess:", get_guessed_word(secret_word, letters_guessed_list))
            guesses += 1
            turns += 1
        else:
            if (letters_guessed_list[turns] in vowels_letters):
                print("Oops! Vowels letter is not in my word:", get_guessed_word(secret_word, letters_guessed_list))
                turns += 1
                guesses -= 1
            else:
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed_list))
                turns += 1
        
        print("------------- \nYou have ",(guesses - turns) ," guesses left.")
        print("Available letters:", get_available_letters(letters_guessed_list), end='')
        letters_guessed_checklist += user_in
    print("\n------------- ")
    turns -= 1
    
    score = (guesses - turns - 1) * len(set(secret_word))
    
    if (is_word_guessed(secret_word, letters_guessed_list)):
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was: ", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    secret_word = 'else'
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
