from game import Game
from gamestate import GameState
import menu

game = Game()

player1 = game.intro()

while game.gamestate != GameState.ENDED:
    if game.gamestate == GameState.MENU:
        menu.display()
        game.gamestate = player1.player_input()
    
