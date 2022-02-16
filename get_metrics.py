from wordle import Wordle
from wordle_solver import WordleSolver

from nltk.corpus import words
from random import randint

if __name__ == "__main__":

    all_words = words.words()
    all_words = list(filter(lambda x:len(x) == 5, all_words))

    TOTAL_PLAYS = 1000
    num_wins = 0
    for i in range(TOTAL_PLAYS):

        rand_idx = randint(0, len(all_words) - 1)
        word = all_words[rand_idx]

        game = WordleSolver(word)

        while not game.wordle.game_over:
            guess = game.random_prediction()
        
        if game.wordle.win:
            num_wins += 1

        print(i)
    
    accuracy = (num_wins / TOTAL_PLAYS) * 100
    print(accuracy)
        


