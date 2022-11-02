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
    words = []
    with open(file, 'r', encoding='utf-8') as input_file:
        words = input_file.readlines()
    words = [word.strip().lower() for word in words]
    answer_list = []
    for word in words:
        if letters[4] in word and len(word) > 3:
            bad_counter = 0
            for letter in word:
                if word.count(letter) > letters.count(letter) or not letter in letters:
                    bad_counter += 1
            if bad_counter == 0 and word not in answer_list:
                answer_list.append(word)
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
    return answer_list

def results():
    """
    Function
    """
