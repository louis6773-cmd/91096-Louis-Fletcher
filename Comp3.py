"""
90196 Louis Fletcher
Component 3 - Upgrade class
"""
 
# the Upgrade class stores the data for a single upgrade
class Upgrade:
   def __init__(self, name, cost, power_increase):
       # name of the upgrade shown on the button
       self.name = name
 
       # how much currency it costs to buy
       self.cost = cost
 
       # how much click power it adds when bought
       self.power_increase = power_increase
 
       # tracks whether the player already owns this upgrade
       self.owned = False
 
 
# quick test to make sure the class works
if __name__ == "__main__":
   upgrade1 = Upgrade("Better Clicks", 10, 1)
 
   print("Name:", upgrade1.name)
   print("Cost:", upgrade1.cost)
   print("Power increase:", upgrade1.power_increase)
   print("Owned:", upgrade1.owned)
 
   # simulate buying the upgrade
   upgrade1.owned = True
   print("Owned after purchase:", upgrade1.owned)
 