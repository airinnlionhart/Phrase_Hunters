# Create your Game class logic in here.
from phrase import *

class Game():
    """"""

    def __init__(self):
        self.phrase = " "
        self.charChecks = Character(" ")

    def title():
        print("Hangman")

    def start():
        self.phrase = random_phrase.list_of_phrases[random.randrange(len(g1.list_of_phrases))]
        theWord = ""
        for a_letter in phrase:
            if a_letter == " ":
                theWord += " "
            else:
                theWord += "-"
        lives = 5
        print(theWord)
        while True:
            count = 0
            guess = input("Guess a leter:" )
            charChecks.guess_validation(guess)
            charChecks.duplicate_check(guess)
            if charChecks.valid and charChecks.was_guessed == False:
                for letter in phrase:
                    if guess in letter:
                        theWord = theWord[:count] + guess + theWord[count + 1:]
                        count += 1
                    else:
                        count += 1
                if guess not in phrase or guess not in theWord:
                    lives -= 1
                    print("You have "+str(lives)+" left")
                print(theWord)
                if "-" not in theWord:
                    print("YOU WON!")
                    break
                if lives == 0:
                    print("You lost this time but try agin")
                    break
            else:
                print("woops either you have guessed it or it is not a single character try again")

              
