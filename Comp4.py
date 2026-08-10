"""
90196 Louis Fletcher
Component 4 - On Click function
"""
import tkinter as tk

# stores all player progress (simplified for func)
class Player:
    def __init__(self):
        self.currency = 0
        self.click_power = 1

    def click(self):
        self.currency = self.click_power
        
def main():
    # creates a new window
    window = tk.Tk()
    window.title("Clicker Game")
    window.geometry("450x250")

    # creates the player object that holds the game data
    player = Player()

    # title label at top
    title_label = tk.Label(window, text="Clicker Game", font=("Arial", 16, "bold"))
    title_label.place(x=50, y=50)

    # coins display below the button
    coin_label = tk.Label(window, text="Coins: 0", font=("Arial", 11))
    coin_label.place(x=100, y=100)

    

        


