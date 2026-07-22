"""
90196 Louis Fletcher
Component 1 - GUI foundation
"""
import tkinter as tk

def main():
    # creates a new window
    window = tk.Tk()
    window.title("Clicker Game")
    window.geometry("450x250")

    # title label at top
    title_label = tk.Label(window, text="Clicker Game", font=("Arial", 16, "bold"))
    title_label.place(x=80, y=10)

    # primary click button
    click_button1 = tk.Button(window, text="button", height=3, width=12)
    click_button1.place(x=90, y=60)

    # coins display below the button
    coin_label = tk.Label(window, text="Coins: 0", font=("Arial", 11))
    coin_label.place(x=105, y=130)

    # currency per click display below coins
    power_label = tk.Label(window, text="+1 / click", font=("Arial", 9), fg="gray")
    power_label.place(x=110, y=155)
    
    # upgrades section header
    upg_label = tk.Label(window, text="Upgrades", font=("Arial", 12, "underline"))
    upg_label.place(x=290, y=20)

    # upgrade buttons
    upg_button1 = tk.Button(window, text="upg1\ncost: ??", width=12)
    upg_button1.place(x=280, y=55)

    upg_button2 = tk.Button(window, text="upg2\ncost: ??", width=12)
    upg_button2.place(x=280, y=110)    

    window.mainloop()

if __name__ == "__main__":
    main()