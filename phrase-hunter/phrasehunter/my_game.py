# Create your Game class logic in here.
from .phrase import Phrase
from .character import Character
import random

class Game():
    """"""

    def __init__(self):
        self.random_phrase = " "
        

    def title(self):
        print("Hangman")

    def start(self):
        pick_phrase = Phrase("hope you can guess this")
        pick_phrase.add_to("try to guess a correct phrase")
        random_phrase = pick_phrase.list_of_phrases[random.randrange(len(pick_phrase.list_of_phrases))]
        theWord = ""
        for a_letter in random_phrase:
            if a_letter == " ":
                theWord += " "
            else:
                theWord += "-"
        lives = 5
        print(theWord)
        charChecks = Character(" ")
        while True:
            count = 0
            guess = input("Guess a leter:" ).lower()
            charChecks.guess_validation(guess)
            charChecks.duplicate_check(guess)
            if charChecks.valid == True and charChecks.was_guessed == False:
                for letter in random_phrase:
                    if guess in letter:
                        theWord = theWord[:count] + guess + theWord[count + 1:]
                        count += 1
                    else:
                        count += 1
                if guess not in random_phrase or guess not in theWord:
                    lives -= 1
                    print("You have "+str(lives)+" left")
                print(theWord)
                if "-" not in theWord:
                    print("YOU WON!")
                    keep_playing = input("Press enter to play again or type q to quit")
                    if keep_playing == '':
                        self.start()
                        break
                    else:
                         break
                if lives == 0:
                    print("You lost this time but try agin")
                    keep_playing = input("Press enter to play again or type q to quit")
                    if keep_playing == '':
                        self.start()
                        break
                    else:
                         break
            else:
                pass


              

