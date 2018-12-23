import numpy as np
import csv
import random


def read_dictionary():
    with open(r"dcused.txt", "r") as dictionary:
        reader = csv.reader(dictionary)
        dictionary_list = list()

        for row in reader:
            dictionary_list.append(row)
    return dictionary_list


def string_getter():
    word = str()
    while not word:
        word = str(input("Which word would you like to play? "))
        if not word.isalpha():
            word = str()
    word = word.upper()
    return list(word)


def list_maker(word_list):
    guessing_list = list()
    for i in range(len(word_list)):
        guessing_list.append('_')
    print(guessing_list)
    return guessing_list


def replacer(locations, guessing_list, word_list):
    for i in locations:
        guessing_list[i] = word_list[i]


def list_checker(word_list, guessing_list):
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
            replacer(locations, guessing_list, word_list)
        else:
            game_count += -1
        if '_' not in guessing_list:
            win = True
        if game_count == 0:
            lose = True
        print(guessing_list)
        print('You have said the following letters: {}'.format(guesses))
        print('You have got {} guesses left'.format(game_count))
    if win:
        print('Congratulations! You have won. The word was: {}'.format(str(word_list)))
    else:
        print('The word was: {}'.format(str(word_list)))


def computer():
    dict = read_dictionary()
    #print(len(dict))
    range = len(dict)
    word = dict[random.randrange(range)]
    #print(word)
    word_list = list(word[0].upper())
    standard(word_list)

def human():
    word_list = string_getter()
    standard(word_list)

def standard(word_list):
    #print(word_list)
    guessing_list = list_maker(word_list)
    #print(guessing_list)
    list_checker(word_list, guessing_list)

while True:
    game_mode = str(input("Would you like to play against the computer or against another human?: "))
    game_mode = game_mode.upper()
    if game_mode == 'COMPUTER':
        computer()
    elif game_mode == 'HUMAN':
        human()
    else:
        continue


