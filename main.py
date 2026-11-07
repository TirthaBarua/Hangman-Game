from random import choice

words = ['counselor', 'dinosaur', 'heliport', 'breakfast', 'enterpreneeur']
correct_letters = []
incorrect_letters = [] 
tries = 6   
right_answers = 0
game_over = False


def choosen_word(list_of_words):
    choosen_word = choice(list_of_words)
    different_letters = len(set(choosen_word))

    return choosen_word, different_letters  

def ask_for_letter():
    choosen_letter = ''
    is_valid = False
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while not is_valid:
        choosen_letter = input('Please choose a letter: ').lower()
        if choosen_letter in alphabet and len(choosen_letter) == 1:
            is_valid = True
        else:
            print('Invalid letter. Please, try again.')
    return choosen_letter

def show_new_board(choosen_word):
    hidden_list = []


    for letter in choosen_word:
        if letter in correct_letters:
            hidden_list.append(letter)
        else:
            hidden_list.append('-')

    print(' '.join(hidden_list))

def check_letter(choosen_letter, hidden_word, tries, matches):
    end = False

    if choosen_letter in hidden_word:
        correct_letters.append(choosen_letter)
        matches += 1    
    else:
        incorrect_letters.append(choosen_letter)
        tries -= 1  

    if tries == 0:
        end = lose() 
    elif matches == unique_letters:
        end = win(hidden_word) 

    return tries, matches, end

def lose():
    print("You don't have any tries left.")
    print("The Hidden word was: " + words)

    return True

def win(revealed_word):
    print("Congratulations! You found the hidden word: " + revealed_word)

    return True

word, unique_letters = choosen_word(words)  

while not game_over:
    print('\n' + '*' * 20)
    show_new_board(word)
    print('Correct letters: ' + ', '.join(correct_letters))
    print('Incorrect letters: ' + ', '.join(incorrect_letters))
    print('You have ' + str(tries) + ' tries left.')
    letter = ask_for_letter()
    tries, right_answers, game_over = check_letter(letter, word, tries, right_answers) 
    game_over = game_over   