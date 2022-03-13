from gamestate import GameState

class Player:
    def __init__(self, name, class_type, age, sex):
        self.name = name
        self.class_type = class_type
        self.age = age
        self.sex = sex
    
    def player_input(self):
        try:
            num = int(input("Please select an option: "))
            if num == 1:
                x = GameState.MENU
            elif num == 20:
                x = GameState.ENDED
            return x
        except ValueError:
            print("Please input a number.")

        

    