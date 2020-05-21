from .character import *

# Create your Phrase class logic here.
class Phrase():
	def __init__(self, aphrase, **kwargs):
		self.letters = [Character(char) for char in aphrase]
		self.guess = []
		self.valid = False
		self.display_results = "_"
		self.win_game = False

 # The class should include an initializer or def __init__ that receives a phrase parameter and 
 # holds this phrase in an instance attribute on the Phrase object.
 # A phrase should be a collection of Character objects, where each letter of the phrase is a Character() 
 # instance stored inside a collection such as a List.
# Any additional instance attributes you feel you need to store are up to you.
		for key, value in kwargs.items():
			setattr(self, key, value)
	

	def guess_validation(self, guess):
		if len(guess) != 1 or guess.isalpha() == False:
			print("whoops this doesnt look like a valid character try again")
			self.valid = False
		else:
			self.valid = True
			self.guess.append(guess)

	def duplicate_check(self, guessed):
		if guessed in self.guess:
			print("whoops you already guessed it")
			self.valid = False
		else:
			self.valid = True       

	def the_word(self, the_char):
		self.display_results = ""
		for char in self.letters:	
			char.guess_check(the_char)
			self.display_results += (str(char.show_character()))
		return self.display_results
	
	def has_won(self):
		if "_" not in self.display_results:	
			self.win_game = True

    
test = Phrase("this is a test")
		





# The Phrase instance might be responsible for things like: Knowing if the entire phrase has been guessed, 
# Iterating over its collection of Character to allow a guess to be checked using a Character instance method call 
# or to ask the Character object how it should show its letter.

# The instance method names and their implementation are up to you to determine.




