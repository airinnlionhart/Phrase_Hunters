
# Create your Character class logic in here.
class Character():
    """Class to validate user input and check there guesses"""

    def __init__(self, original):
        self.original = original.lower()
        self.was_guessed = False
        self.tryAgain = False


        while True:
            if len(self.original) != 1:
                newGuess = input("Woops not a single letter please enter a single letter: ")
                self.original = newGuess.lower()
            if self.original.isalpha() == False:
                newGuess = input("Woops not a single letter please enter a single letter: ")
                self.original = newGuess.lower()
            else:
                break

    def  guessCheck(self, guessed):
        if guessed == self.original:
            self.was_guessed = True
        else:
            self.was_guessed = False
            self.original = guessed


    def showChar(self):
        if self.was_guessed == True:
            self.tryAgin = True
            print("please try again")
        else:
            print("_")


g1 = Character("a")
g1.guessCheck("b")
g1.showChar()


g1.guessCheck("b")
g1.showChar()

g1.guessCheck("a")
g1.showChar()

g1.guessCheck("a")
g1.showChar()
