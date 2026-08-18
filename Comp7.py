
"""
90196 Louis Fletcher
Component 7 - Save/load functions
"""
import json

# basic player class storing data
class Player:
    def __init__(self):
        self.name = ""
        self.currency = 0
        self.click_power = 1
        self.passive_income = 0


# saving player rpogress to json file
def save_game(player, filename="savefile.json"):
    data = {
        "name": player.name,
        "currency": player.currency,
        "click_power": player.click_power,
        "passive_income": player.passive_income
    }

    with open(filename, "w") as file:
        json.dump(data, file)

    print("Game saved.")
