from config import CONFIG
from tkinter import Button
from idlelib.tooltip import Hovertip

class BUTTON:
    def __init__(_self, root, command, name='', row=0, column=0):
        confirm = Button(root, text=CONFIG['LABELS'][name], command=command, padx=5, pady=5)
        confirm.grid(row=row, column=column)

        Hovertip(confirm, CONFIG['TOOLTIPS'][name])
