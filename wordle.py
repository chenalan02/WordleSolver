class Wordle():

    def __init__(self, word:str):
        self.word = [char for char in word.lower()]
        self.known_letters = set()
        self.eliminated_letters = set()
        self.known_positions = [None] * 5
        self.turn = 0
        self.game_over = False

    def guess(self, guess:str):
        guess = [char for char in guess.lower()]
        new_letters = set()
        new_positions = []

        if len(guess) != 5:
            print("guess must be 5 letters!")
        else:
            self._check_win(guess)
            for i, letter in enumerate(guess):
                new_letter = self._check_letter(letter)
                new_position = self._check_letter_pos(letter, i)
                if new_letter:
                    new_letters.add(new_letter)
                if new_position:
                    new_positions.append(new_position)
            self.turn += 1
            if self.turn > 6:
                self.game_over = True
            
        return new_letters, new_positions
    
    def _check_letter(self, letter):
        if letter in self.word:
            if letter not in self.known_letters:
                self.known_letters.add(letter)
                return (letter, True)
        else:
            if letter not in self.eliminated_letters:
                self.eliminated_letters.add(letter)
                return (letter, False)

    def _check_letter_pos(self, letter, i):
        if self.known_positions[i] == None:
            if self.word[i] == letter:
                self.known_positions[i] = letter
                return (letter, i)

    def _check_win(self, guess:str):
        if guess == self.word:
            self.game_over = True
            print("game win")

    def print_known_letters(self):
        print("known_letters: " + str(self.known_letters))

    def print_known_positions(self):
        print("known_positions: " + str(self.known_positions))
