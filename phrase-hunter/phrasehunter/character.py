
# Create your Character class logic in here.
class Character():
    """Class to validate user input and check there guesses"""

    def __init__(self, original):
        self.original = [original.lower()]
        self.was_guessed = False
        self.valid = False


    def guess_validation(self, guess):
        if len(guess) != 1 or guess.isalpha() == False:
            self.valid = False
        else:
            self.valid = True
        


    def duplicate_check(self, guessed):
        if guessed in self.original:
            self.was_guessed = True
        else:
            self.was_guessed = False
            self.original.append(guessed.lower())
