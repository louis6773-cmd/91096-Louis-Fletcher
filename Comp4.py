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


