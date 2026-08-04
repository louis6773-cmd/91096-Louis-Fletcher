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
    window.minsize(450, 300)
    window.maxsize(450, 300)
    

    # title label at top
    title_label = tk.Label(window, text="Clicker Game", font=("Arial", 16, "bold"))
    title_label.place(x=80, y=10)

    # primary click button
    click_button1 = tk.Button(window, text="button", height=3, width=12)
    click_button1.place(x=90, y=90)

    # coins display below the button
    coin_label = tk.Label(window, text="Coins: 0", font=("Arial", 11))
    coin_label.place(x=105, y=160)

    # currency per click display below coins
    power_label = tk.Label(window, text="+1 / click", font=("Arial", 9), fg="gray")
    power_label.place(x=110, y=185)
    
    # upgrades section header
    upg_label = tk.Label(window, text="Upgrades", font=("Arial", 12, "underline"))
    upg_label.place(x=290, y=40)
    
    # username label 
    user_label = tk.Label(window, text="Username: ", font=("Arial", 10,))
    user_label.place(x=80, y=40)
    
    # username entry box
    user_entry = tk.Entry(window, width=15)
    user_entry.place(x=155, y=42)
    
    # upgrade buttons
    upg_button1 = tk.Button(window, text="upg1\ncost: ??", width=12)
    upg_button1.place(x=280, y=75)

    upg_button2 = tk.Button(window, text="upg2\ncost: ??", width=12)
    upg_button2.place(x=280, y=130)  
    
    upg_button3 = tk.Button(window, text="upg3\ncost: ??", width=12)
    upg_button3.place(x=280, y=185)    

    # save/load buttons
    save_button = tk.Button(window, text="save", width=7)
    save_button.place(x=75, y=230)
    
    load_button = tk.Button(window, text="load", width=7)
    load_button.place(x=140, y=230)        

    window.mainloop()

if __name__ == "__main__":
    main()