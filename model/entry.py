from config import CONFIG
from tkinter import Entry, Label
from idlelib.tooltip import Hovertip

import tkinter as tk
import re

class ENTRY:
    def __init__(_self, root, frame, name, row, width=50, borderwidth=0, font=('Arial', 12), padx=0, pady=0):
        vcmd = (root.register(_self.validate), '%P')
        ivcmd = (root.register(_self.on_invalid),)

        _self.entry = Entry(frame, width=width, borderwidth=borderwidth)
        _self.entry.grid(row=row, column=1)
        _self.entry.config(validate='focusout', validatecommand=vcmd, invalidcommand=ivcmd)

        Label(frame, text=CONFIG['LABELS'][name], font=font).grid(row=row, column=0, padx=padx, pady=pady)
        Hovertip(_self.entry, CONFIG['TOOLTIPS'][name])

        _self.label_error = Label(frame, foreground='red')
        _self.label_error.grid(row=row, column=3, sticky=tk.W, padx=5)

    def show_message(self, error='', color='black'):
        self.label_error['text'] = error
        self.entry['foreground'] = color

    def validate(_self, value):
        """
        Validate entry
        Only numbers allowed
        :param value:
        :return boolean:
        """
        if re.fullmatch(r'^[0-9]*$', value) is None:
            return False

        _self.show_message()
        return True

    def on_invalid(_self):
        """
            Show error message if data invalid
            :return None:
        """
        _self.show_message('Please enter a valid value', 'red')