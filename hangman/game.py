from .exceptions import *
from random import choice

# Complete with your own, just for fun :)
LIST_OF_WORDS = []


def _get_random_word(list_of_words):

    if not list_of_words:
        raise InvalidListOfWordsException()

    return choice(list_of_words)


def _mask_word(word):

    if not word:
        raise InvalidWordException()

    else:
        masked_word = '*' * len(word)

    return masked_word


def _uncover_word(answer_word, masked_word, character):

    if not answer_word or not masked_word :
        raise InvalidWordException()

    elif len(answer_word) != len(masked_word):
        raise InvalidWordException()

    elif len(character) != 1:
        raise InvalidGuessedLetterException()

    else:

        answer_word = answer_word.lower()
        character = character.lower()

        if character in answer_word:
            for index, letter in enumerate(answer_word):
                if letter == character:
                    masked_word = masked_word[:index] + character + masked_word[index+1:]

    return masked_word


def guess_letter(game, letter):

    if game['remaining_misses'] <= 0 or '*' not in game['masked_word']:
        raise GameFinishedException()

    else:
        answer_word = game['answer_word']
        masked_word = game['masked_word']

        new_masked_word = _uncover_word(answer_word, masked_word, letter)
        game['masked_word'] = new_masked_word

        if new_masked_word == answer_word:
            raise GameWonException()

        else:

            if letter not in game['previous_guesses']:
                game['previous_guesses'].append(letter.lower())

            if new_masked_word == masked_word:
                game['remaining_misses'] -= 1

            if game['remaining_misses'] == 0:
                raise GameLostException()


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
