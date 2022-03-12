import pygame
import config
from game import Game
from gamestate import GameState

pygame.init()

screen = pygame.display.set_mode([600,400])

pygame.display.set_caption("Pokemon Clone")

clock = pygame.time.Clock()

game = Game(screen)

game.set_up()


while game.gamestate == GameState.RUNNING:
    clock.tick(50)
    game.update()
    pygame.display.flip()
