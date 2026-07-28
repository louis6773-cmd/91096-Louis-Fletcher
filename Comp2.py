"""
90196 Louis Fletcher
Component 2 - Player class
"""

# the Player class stores all the data about the player's progress
class Player:
    def __init__(self):
        # currency the player currently has
        self.currency = 0

        # how much currency is earned per click
        self.click_power = 1

        # how much currency is earned automatically per second
        self.passive_income = 0

    # adds currency when the player clicks the button
    def click(self):
        self.currency += self.click_power

    # adds currency automatically (used later for passive income)
    def earn_passive(self):
        self.currency += self.passive_income
        
# test code
if __name__ == "__main__":
    player = Player()

    print("Starting currency:", player.currency)
    
    # adding currency
    player.click()
    print("After 1 click:", player.currency)

    # altering click power adding currency
    player.click_power = 5
    player.click()
    print("After click power upgrade + 1 click:", player.currency)
    
    

