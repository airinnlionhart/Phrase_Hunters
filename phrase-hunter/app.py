# Import your Game class
from phrasehunter.game import Game
import random

list_of_phrases = ["can you guess this phrase", "this game is fun", "not that happy with this code"]

# Create your Dunder Main statement.
if __name__ == "__main__":
# Inside Dunder Main:
## Create an instance of your Game class
	while True:
		print("Welcome")
		start_game = Game(list_of_phrases[random.randrange(len(list_of_phrases))])
	## Start your game by calling the instance method that starts the game loop
		start_game.title()
		start_game.start_game()
		keep_playing = input("Press enter to play again or type q to quit")
		if keep_playing == '':
			pass
		else:
			break