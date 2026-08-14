"""
90196 Louis Fletcher
Component 6 - Autoclicker function
"""

import tkinter as tk

# basic class storing player data
class Player:
    def __init__(self):
        self.currency = 0 
        self.passive_income = 2

def main():
    # window dimensions
    window = tk.Tk()
    window.title("Clicker Game")
    window.geometry("450x250")

    window.mainloop()

if __name__ == "__main__":
    main()
