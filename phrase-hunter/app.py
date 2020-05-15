# Import your Game class
from phrasehunter.game import Game


# Create your Dunder Main statement.
if __name__ == "__main__":
# Inside Dunder Main:
## Create an instance of your Game class
    start_game = Game()
## Start your game by calling the instance method that starts the game loop
    start_game.title()
    start_game.start()
