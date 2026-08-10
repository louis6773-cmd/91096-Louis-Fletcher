"""
90196 Louis Fletcher
Component 5 - Buy Upgrade function
"""

# checks whether the player can afford the upgrade
def buy_upgrade(player, upgrade):
    if player.currency >= upgrade.cost:
        print("Can afford this upgrade")
    else:
        print("cannot afford this upgrade")
        

