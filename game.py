import pygame
import config
from player import Player
from gamestate import GameState

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.gamestate = GameState.NONE

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.gamestate = GameState.RUNNING
        print("do set up")
    
    def update(self):
        self.screen.fill(config.BLACK)
        self.handle_events()

        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gamestate = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gamestate = GameState.ENDED
                elif event.key == pygame.K_w:
                    self.player.update_position(0, -1)
                elif event.key == pygame.K_s:
                    self.player.update_position(0, 1)
                elif event.key == pygame.K_a:
                    self.player.update_position(-1, 0)
                elif event.key == pygame.K_d:
                    self.player.update_position(1, 0)
