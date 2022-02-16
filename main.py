from wordle import Wordle
from wordle_solver import WordleSolver

from nltk.corpus import words
from random import randint

if __name__ == "__main__":
    all_words = words.words()
    all_words = list(filter(lambda x:len(x) == 5, all_words))
    rand_idx = randint(0, len(all_words) - 1)
    word = all_words[rand_idx]
    print(word)
    wordle = WordleSolver(word)
    while not wordle.wordle.game_over:
        guess = wordle.random_prediction()
        print("guess: " + guess)
        print(len(wordle.word_base))
    
    wordle.print_word_base()

