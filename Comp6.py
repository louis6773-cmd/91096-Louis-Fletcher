"""
90196 Louis Fletcher
Component 6 - Autoclicker function
"""

import tkinter as tk

# basic class storing player data
class Player:
    def __init__(self):
        self.currency = 0 
        self.passive_income = 1

def main():
    # window dimensions
    window = tk.Tk()
    window.title("Clicker Game")
    window.geometry("50x50")
    
    player = Player()
    
    # tracks whether the passive income loop has already started
    loop_started = False
    
    # coisn display
    coin_label = tk.Label(window, text="Coins: 0", font=("Arial", 11))
    coin_label.place(x=20, y=20)
    
    # adds passive income and updates label
    def passive_tick():
        player.currency += player.passive_income
        coin_label.config(text="coins: " + str(player.currency))
        window.after(1000, passive_tick)
    
    # only starts the loop if it hasn't already been started
    def start_passive_income():
        nonlocal loop_started
        if not loop_started:
            loop_started = True
            passive_tick()
    
    # starts the passive income loop 
    start_passive_income()    

    window.mainloop()

if __name__ == "__main__":
    main()
