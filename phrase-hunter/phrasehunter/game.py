# Create your Game class logic in here.
from .phrase import Phrase
from .character import Character
import random

class Game():
    """The class should include an initializer or def __init__ method that receives a 
    phrases parameter and holds these phrases in an instance attribute on the game object."""

    def __init__(self, phrases):
        self.game = [Phrase(phrases.lower())]
        self.current_phrase = self.game[random.randrange(len(self.game))]
        self.current_lives = 5
      
    def title(self):
        print("Welecome to Phrase Hunters you mission is to guess the phrase one character at a time before your five lives run out")
        print(self.current_phrase.the_word(''))   

    def start_game(self):

        while True:
            self.current_phrase.has_won() 
            if self.current_phrase.win_game:
                print("You have Won!!! great job!!!")
                break
            elif self.current_lives == 0:
                print("Your are out of lives try again")
                break        
            else:        
                guess = input("guess a letter: ")
                self.current_phrase.duplicate_check(guess)
                if self.current_phrase.valid:
                    self.current_phrase.guess_validation(guess)
                else:
                    pass
                if self.current_phrase.valid:
                    before = self.current_phrase.display_results
                    print(self.current_phrase.the_word(guess))
                    after = self.current_phrase.display_results
                    if before == after:
                        self.current_lives -= 1
                        print("Sorry that letter is not in the Phrase you have " + str(self.current_lives) + " lives remains")
                else:
                    pass


        
# You will need at least 1 instance attribute to start the game:

# An instance attribute that stores the current Phrase object and starts the game. You may think of this as the Active phrase being guessed against by the player while the game is running.
# The Game instance might be responsible for things like: starting the game loop, getting player's input() guesses to pass to a Phrase object to perform its responsibilities against, determining if a win/loss happens after the player runs out of turns or the phrase is completely guessed.

