import tkinter as tk
import time

wn = tk.Tk()
wn.geometry('800x350')
wn.title('Elf Game 2')
wn.config(background='lightblue')

class game:
    def __init__(self):
        pass

    def update(self):
        pass

    def clicked(self):
        print("clicked")

    def setup_ui(self):
        n1 = tk.Entry(wn, width=30, text='Enter team name 1')
        n2 = tk.Entry(wn, width=30, text='Enter team name 2')
        n3 = tk.Entry(wn, width=30, text='Enter team name 3')
        n4 = tk.Entry(wn, width=30, text='Enter team name 4')
        n1.grid(row=0, column=0)
        n2.grid(row=0, column=1)
        n3.grid(row=0, column=2)
        n4.grid(row=0, column=3)
        
game = game()
game.setup_ui()

wn.mainloop()

