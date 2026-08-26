"""
90196 Louis Fletcher
Final merge, completed clicker game, merging all components into one
"""
import tkinter as tk
import json

# stores all the data about the player's progress
class Player:
    def __init__(self):
        self.name = ""
        # currency the player currently has
        self.currency = 0
        # how much currency is earned per click
        self.click_power = 1
        # how much currency is earned automatically per second
        self.passive_income = 0

    # adds currency when the player clicks the button
    def click(self):
        self.currency += self.click_power

    # adds currency automatically, used for auotclicker
    def earn_passive(self):
        self.currency += self.passive_income

    # sets the player's name, with basic input validation
    def set_name(self, name):
        name = name.strip()

        # reject empty input
        if name == "":
            print("Username invalid")
            return False

        # check if username is too long
        if len(name) > 15:
            print("Name is too long (max 15)")
            return False

        self.name = name
        return True

# stores the data for a single upgrade
class Upgrade:
    def __init__(self, name, cost, power_increase, passive_increase=0):
        # name of the upgrade shown on the button
        self.name = name
        # how much currency it costs to buy
        self.cost = cost
        # how much click power it adds when bought
        self.power_increase = power_increase
        # how much passive income this upgrade (essentially just for AC)
        self.passive_increase = passive_increase
        # tracks whether the player already owns this upgrade
        self.owned = False

# saving player progress to json file
def save_game(player, upgrades, filename="savefile.json"):
    data = {
        "name": player.name,
        "currency": player.currency,
        "click_power": player.click_power,
        "passive_income": player.passive_income,
        # saves whiuch upgrades have been bought by their name
        "owned_upgrades": [u.name for u in upgrades if u.owned]
    }

    with open(filename, "w") as file:
        json.dump(data, file)
    print("Game saved.")

# loads player progress from a json file
def load_game(upgrades, filename="savefile.json"):
    player = Player()
    # accesses and extracts the data and starts a new game if nonexistant
    try:
        with open(filename, "r") as file:
            data = json.load(file)
        player.name = data.get("name", "")
        player.currency = data.get("currency", 0)
        player.click_power = data.get("click_power", 1)
        player.passive_income = data.get("passive_income", 1)

        # restores the owned upgrades so they show up as bought again
        owned_names = data.get("owned_upgrades", [])
        for u in upgrades:
            if u.name in owned_names:
                u.owned = True

        print("Game loaded.")

    # resets when file not found
    except FileNotFoundError:
        print("No save file found, starting new game.")

    return player


def main():
    # creates a new window
    window = tk.Tk()
    window.title("NCEA Simulator")
    # setting the dimensions of the created window
    window.geometry("450x330")
    window.minsize(450, 330)
    window.maxsize(450, 330)
    #slate blue
    window.configure(bg="#5c699c")

    # player and upgrades are created HERE so every func below can use them
    player = Player()
    upgrades = [
        Upgrade("Merit Endorsement", 30, 1),
        Upgrade("Excellence Endorsement", 90, 3),
        Upgrade("Scholarship", 900, 5),
        Upgrade("Passive credits (+1/s)", 300, 0, passive_increase=1)
    ]

    # title label at top
    title_label = tk.Label(window, text="NCEA Simulator", font=("Arial", 16, "bold"))
    title_label.place(x=80, y=10)

    # coins display below the button
    coin_label = tk.Label(window, text="Coins: 0", font=("Arial", 11))
    coin_label.place(x=105, y=170)

    # currency per click display below coins
    power_label = tk.Label(window, text="+1 / click", font=("Arial", 9), fg="gray")
    power_label.place(x=110, y=195)

    # upgrades section header
    upg_label = tk.Label(window, text="Upgrades", font=("Arial", 12, "underline"))
    upg_label.place(x=290, y=40)

    # username label
    user_label = tk.Label(window, text="Username: ", font=("Arial", 10))
    user_label.place(x=10, y=40)

    # username display
    userdisplay_label = tk.Label(window, text="Username: __________", font=("Arial", 10))
    userdisplay_label.place(x=10, y=60)

    # username entry box
    user_entry = tk.Entry(window, width=12)
    user_entry.place(x=95, y=42)

    # new feedback label
    status_label = tk.Label(window, text="", font=("Arial", 9), fg="red")
    status_label.place(x=10, y=85)

    # wiring the set button to set_name, linking to GUI entry box
    def on_set_name():
        typed_name = user_entry.get()
        if player.set_name(typed_name):
            userdisplay_label.config(text="Username: " + player.name)
            status_label.config(text="")
        else:
            status_label.config(text="Invalid username")

    # sets up button
    set_name_button = tk.Button(window, text="Set", width=6, command=on_set_name)
    set_name_button.place(x=205, y=40)

    # function runs everytime button is pressed
    def on_click():
        # adds currency using the player's click power
        player.click()
        # updates the coin label so the change shows straight away
        coin_label.config(text="Coins: " + str(player.currency))

    # primary click button linked to the on_click function
    click_button1 = tk.Button(window, text="🟢BUTTON🟢", height=3, width=12, command=on_click)
    click_button1.place(x=90, y=100)

    # checks whether the player can afford the upgrade
    def buy_upgrade(upgrade, button):
        # don't allow buying same upgrade twice
        if upgrade.owned:
            status_label.config(text="Already owned")
            return

        if player.currency >= upgrade.cost:
            # subtract the cost from the player's currency
            player.currency -= upgrade.cost
            # apply upgrade's effect
            player.click_power += upgrade.power_increase
            # applies passive income for the autoclicker upgrade
            player.passive_income += upgrade.passive_increase
            upgrade.owned = True

            # update the coins for player feedback
            coin_label.config(text="Coins: " + str(player.currency))
            power_label.config(text="+" + str(player.click_power) + " / click")
            button.config(text="Bought")
            status_label.config(text="")

            # starts autoclikcer loop if upgrade adds passive income (again, solely for AC)
            if upgrade.passive_increase > 0:
                start_passive_income()
        else:
            # gives feedback instead of disabling the button
            status_label.config(text="Not enough currency")

    # creates all 4 upgrade buttons in a LOOP, u=upgrade and b=btn - avoids lambda bug
    upgrade_buttons = []
    y_position = 65
    for upgrade in upgrades:
        btn = tk.Button(window, text=upgrade.name + "\ncost: " + str(upgrade.cost), width=14)
        btn.config(command=lambda u=upgrade, b=btn: buy_upgrade(u, b))
        btn.place(x=280, y=y_position)
        upgrade_buttons.append(btn)
        y_position += 50
        
        
    # tracks whether the passive income loop has already started
    loop_started = False
    # for autoclicker , adds passive income and updates label
    def passive_tick():
        player.earn_passive()
        coin_label.config(text="Coins: " + str(player.currency))
        window.after(1000, passive_tick)

    # only starts the loop if it hasn't already been started
    def start_passive_income():
        nonlocal loop_started
        if not loop_started:
            loop_started = True
            passive_tick()
            

    # save/load feature, links the save/load functions to the GUI buttons
    def on_save():
        save_game(player, upgrades)
        status_label.config(text="Game saved")

    def on_load():
        loaded_player = load_game(upgrades)
        # copy loaded values onto the existing player object
        player.name = loaded_player.name
        player.currency = loaded_player.currency
        player.click_power = loaded_player.click_power
        player.passive_income = loaded_player.passive_income

        # refresh all labels and upgrade buttons to match loaded data
        coin_label.config(text="Coins: " + str(player.currency))
        power_label.config(text="+" + str(player.click_power) + " / click")
        userdisplay_label.config(text="Username: " + (player.name if player.name else "__________"))

        # loads bought upgrades 
        for upgrade, button in zip(upgrades, upgrade_buttons):
            if upgrade.owned:
                button.config(text="Bought")

        # restarts the autoclicker loop if the loaded save already had passive income
        if player.passive_income > 0:
            start_passive_income()

        status_label.config(text="Game loaded")

    # save/load buttons
    save_button = tk.Button(window, text="save", width=7, command=on_save)
    save_button.place(x=75, y=250)

    load_button = tk.Button(window, text="load", width=7, command=on_load)
    load_button.place(x=140, y=250)

    window.mainloop()


if __name__ == "__main__":
    main()
