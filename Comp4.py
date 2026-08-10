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
        self.currency += self.click_power
        
def main():
    # creates a new window
    window = tk.Tk()
    window.title("Clicker Game")
    window.geometry("250x250")

    # creates the player object that holds the game data
    player = Player()

    # title label at top
    title_label = tk.Label(window, text="Clicker Game", font=("Arial", 15, "bold"))
    title_label.place(x=60, y=30)

    # coins display below the button
    coin_label = tk.Label(window, text="Coins: 0", font=("Arial", 11))
    coin_label.place(x=100, y=150)
    
    # function runs everytime butto is pressed
    def on_click():
        # adds currency using the player's click power
        player.click()

        # updates the coin label so the change shows straight away
        coin_label.config(text="Coins: " + str(player.currency))

    # primary click button linked to the on_click function
    click_button1 = tk.Button(window, text="button", height=3, width=12, command=on_click)
    click_button1.place(x=90, y=70)

    window.mainloop()

if __name__ == "__main__":
    main()

    

        


