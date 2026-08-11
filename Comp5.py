"""
90196 Louis Fletcher
Component 5 - Buy Upgrade function
"""
# stores all data on player’s progress
class Player:
    def __init__(self):
        self.currency = 0
        self.click_power = 1

# stores all data on upgrades
class Upgrade:
    def __init__(self, name, cost, power_increase):
        self.name = name
        self.cost = cost
        self.power_increase = power_increase
        self.owned = False

# checks whether the player can afford the upgrade
def buy_upgrade(player, upgrade):
    if player.currency >= upgrade.cost:
        # subtract the cost from the player's currency
        player.currency -= upgrade.cost
        # apply upgrade's effect
        player.click_power += upgrade.power_increase
        upgrade.owned = True

        print("Upgrade purchased")
    else:
        print("Cannot afford this upgrade")




