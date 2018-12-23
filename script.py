import numpy as np

global word_list
global guessing_list
#maardananders


def string_getter():
    word = str()
    while not word:
        word = str(input("Which word would you like to play? "))
        if ' ' in word:
            word = str()
    word = word.upper()
    return list(word)


def list_maker():
    guessing_list = list()
    for i in range(len(word_list)):
        guessing_list.append('_')
    print(guessing_list)
    return guessing_list


def replacer(locations):
    for i in locations:
        guessing_list[i] = word_list[i]


def list_checker():
    win = lose = False
    values = np.array(word_list)
    game_count = 8
    guesses = list()
    while not win and not lose:
        letter = str(input("Guess a letter: "))
        if len(letter) > 1:
            continue
        guesses.append(letter)
        guesses.sort()
        letter = letter.upper()
        if letter in word_list:
            locations = np.where(values == letter)[0]
            replacer(locations)
        else:
            game_count += -1
        if '_' not in guessing_list:
            win = True
        if game_count == 0:
            lose = True
        print(guessing_list)
        print('You have said the following letters: {}'.format(guesses))
        print('You have got false {} guesses left'.format(game_count))
    if win:
        print('Congratulations! You have won. The word was: {}'.format(str(word_list)))


word_list = string_getter()
guessing_list = list_maker()
list_checker()
