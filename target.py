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
    alp = string.ascii_uppercase
    for i in range(3):
        in_list = []
        for j in range(3):
            n = random.randrange(0, 26)
            in_list.append(alp[n])
        random_list.append(in_list)
    return random_list

def get_words(file: str, letters: List[str]) -> List[str]:
    """
    Reads the file file. Checks the words with rules and returns a list of words.
    """
    with open(file, 'r', encoding='utf-8') as input_file:
        words = input_file.readlines()
    words = [word.strip() for word in words]
    answer_list = []
    for i in letters:
        if i in words:
            answer_list.append(i)
    return answer_list

def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    pass


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
