from wordle import Wordle
from wordle_solver import WordleSolver

from nltk.corpus import words
from random import randint

if __name__ == "__main__":

    all_words = words.words()
    all_words = list(filter(lambda x:len(x) == 5, all_words))
    rand_idx = randint(0, len(all_words) - 1)
    word = all_words[rand_idx]
    print("word: " + word)

    game = WordleSolver(word)
    guess_num = 1
    while not game.wordle.game_over:
        guess = game.random_prediction()
        print("guess "+str(guess_num)+": " + guess)
        if not game.wordle.win:
            print("remaining words: " + str(len(game.word_base)))
        guess_num += 1
    
    if game.wordle.win:
        print("GAME WON")
    else:
        print("GAME LOST")
        print("remaining word base:")
        game.print_word_base()

