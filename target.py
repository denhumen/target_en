"""
Module includes functions
generate_grid(), get_words(),
get_user_words(), get_pure_user_words,
results()
Module = target game
"""
from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    random_list = []
    alp = string.ascii_lowercase
    sil = 0
    for i in range(3):
        sil += i
        in_list = []
        for j in range(3):
            sil += j
            random_n = random.randrange(0, 26)
            in_list.append(alp[random_n])
        random_list.append(in_list)
    return random_list

def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file file. Checks the words with rules and returns a list of words.
    """
    with open(file, 'r', encoding='utf-8') as input_file:
        words = input_file.readlines()
    words = [word.strip().lower() for word in words]
    answer_list = []
    for i in words:
        if i.count(letters[4]) == 0:
            continue
        counter = 0
        for j in i:
            if letters.count(j) == 0:
                counter += 1
            elif i.count(j) > letters.count(j):
                counter += 1
        if counter > 0:
            continue
        answer_list.append(i)
    return answer_list

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    input_words = []
    letter = 'f'
    print("Write down words:")
    while letter != '':
        letter = input()
        if letter == '':
            break
        input_words.append(letter)
    return input_words

def get_pure_user_words(user_words: List[str],
                        letters: List[str],
                        words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    answer_list = []
    letters_tuple = set()
    for i in letters:
        letters_tuple.add((i, letters.count(i)))
    letters_tuple = sorted(list(letters_tuple))
    string_letters = ''
    for tuple_ in letters_tuple:
        string_letters += tuple_[0]
    for i in user_words:
        if i.count(letters[4]) == 0:
            continue
        word_tuple = set()
        for j in i:
            word_tuple.add((j, i.count(j)))
        word_tuple = sorted(list(word_tuple))
        bad_counter = 0
        for j in word_tuple:
            if string_letters.count(j[0]) == 0:
                bad_counter += 1
            for k in letters_tuple:
                if j[0] == k[0] and j[1] > k[1]:
                    bad_counter += 1
        if bad_counter > 0:
            continue
        if i not in words_from_dict:
            answer_list.append(i)
    return answer_list

def results():
    """
    Function
    """
    pass
