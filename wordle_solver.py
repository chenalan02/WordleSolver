from nltk.corpus import words
from wordle import Wordle
from random import randint

class WordleSolver():

    def __init__(self, word):
        self.wordle = Wordle(word)
        self.word_base = words.words()
        self.word_base = filter(lambda x:len(x) == 5, self.word_base)
        self.word_base = list(map(lambda word:[char for char in word.lower()], self.word_base))

    def _filter_letter(self, letter, known:bool):
        if known:
            self.word_base = list(filter(lambda word:letter in word, self.word_base))
        else:
            self.word_base = list(filter(lambda word:letter not in word, self.word_base))

    def _filter_position(self, letter, i):
        self.word_base = list(filter(lambda word:word[i] == letter, self.word_base))

    def guess(self, guess):
        new_letters, new_positions = self.wordle.guess(guess)
        for letter, known in new_letters:
            self._filter_letter(letter, known)
        for letter, i in new_positions:
            self._filter_position(letter, i)

    def random_prediction(self):
        rand_idx = randint(0, len(self.word_base) - 1)
        guess = self.word_base[rand_idx]
        guess = "".join(guess)
        self.guess(guess)
        return guess

    def print_word_base(self):
        print(list(map(lambda word:"".join(word), self.word_base)))
