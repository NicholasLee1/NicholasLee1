from enum import Enum

class GameState(Enum):
    GAMESTATE = 0
    RUNNING = 10
    ENDED = 20
    
    MENU = 1
    QUEST = 2
    INVENTORY = 3
    STATS = 4

