"""
90196 Louis Fletcher
Component 5 - Buy Upgrade function
"""
import tkinter as tk

# stores all data on player’s progress
class Player:
    def __init__(self):
        self.currency = 20
        self.click_power = 1

# stores all data on upgrades
class Upgrade:
    def __init__(self, name, cost, power_increase):
        self.name = name
        self.cost = cost
        self.power_increase = power_increase
        self.owned = False

# checks whether the player can afford the upgrade
def buy_upgrade(player, upgrade, button, status_label, coin_label):
    # don't allow buying same upgrade twice
    if upgrade.owned:
        status_label.config(text="Already owned")
        return        
    if player.currency >= upgrade.cost:
        # subtract the cost from the player's currency
        player.currency -= upgrade.cost
        
        # apply upgrade's effect        
        player.click_power += upgrade.power_increase
        upgrade.owned = True
        
        # update the coins for player feedback
        coin_label.config(text=f"Coins: {player.currency}")
        button.config(text="bought")
        status_label.config(text="")
    else:
        # gives feedback instead of disabling the button
        status_label.config(text="not enough currency")


def main():
    window = tk.Tk()
    window.title("clicker game test")
    window.geometry("450x250")

    player = Player()
    upgrade1 = Upgrade("Better clicks", 10, 1)

    # sets initial coins from player.currency
    coin_label = tk.Label(window, text=f"Coins: {player.currency}", font=("Arial", 11))
    coin_label.place(x=30, y=20)

    status_label = tk.Label(window, text="", font=("Arial", 9))
    status_label.place(x=20, y=180)

    upg_button1 = tk.Button(window, text="better clicks\ncost: 10", width=15)
    # passed coin_label to buy_upgrade
    upg_button1.config(command=lambda: buy_upgrade(player, upgrade1, upg_button1, status_label, coin_label))
    upg_button1.place(x=30, y=55)

    window.mainloop()

if __name__ == "__main__":
    main()