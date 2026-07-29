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
        
    # sets the player's name, with basic input validation
    def set_name(self, name):
        name = name.strip() 
        
        # reject empty input
        if name == "":
            print("Username invalid")
            return False
  
        # check if username is too long
        if len(name) > 15:
            print("Name is too long (max 15")
            return False
        
        self.name = name
        return True
        
      
# test code
if __name__ == "__main__":
    player = Player()

    # displaying current currency
    print("Starting currency:", player.currency)
    
    # adding currency
    player.click()
    print("After 1 click:", player.currency)

    # altering click power adding currency
    player.click_power = 5
    player.click()
    print("After click power upgrade + 1 click:", player.currency)
  
    # test name input including boundary cases
    print("Testing username:")
    print("Valid name:", player.set_name("Louis"))
    print("Empty name:", player.set_name("")) 
    print("Spaces only:", player.set_name("   "))
    print("Too long:", player.set_name("rgjdfjgdlfkjeeeee"))
    print("Current name:", player.name)