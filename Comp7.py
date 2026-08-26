
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

# loads player progress FROM a json file
def load_game(filename="savefile.json"):
    player = Player()
    # try/except statements to access and extract the data, and starts new game if non existent
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        player.name = data.get("name", "")
        player.currency = data.get("currency", 0)
        player.click_power = data.get("click_power", 1)
        player.passive_income = data.get("passive_income", 0)

        print("Game loaded.")

    except FileNotFoundError:
        print("No save file found, starting new game.")

    return player

# throaway test code
if __name__ == "__main__":
    player = Player()
    player.name = "louis"
    player.currency = 50
    player.click_power = 3
    player.passive_income = 2

    save_game(player)

    loaded_player = load_game()
    print("Loaded name:", loaded_player.name)
    print("Loaded currency:", loaded_player.currency)
    print("Loaded click power:", loaded_player.click_power)
    print("Loaded passive income:", loaded_player.passive_income)