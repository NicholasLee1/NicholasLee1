from player import Player
from gamestate import GameState

class Game:
    def __init__(self):
        self.gamestate = GameState.GAMESTATE

    def intro(self):
        name = input("What is your name? ")
        class_type = input("What class would you like to be? ")
        age = input("How old are you? ")
        sex = input("What is your gender? ")
        player = Player(name, class_type, age, sex)

        print("This is the beginning of the story!")
        print(f"Your name is {player.name} and you are a(n) {player.class_type}. You are a {player.age} year old {player.sex}")
        self.gamestate = GameState.MENU

        return player
