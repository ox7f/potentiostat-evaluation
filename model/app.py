from config import CONFIG

from model.frame import FRAME
from model.button import BUTTON
from model.graph import Graph
from model.menu import MENU

import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    menu = None
    frames = []
    frame_data = []
    active_tab = 0
    active_frame = None
    data = []

    # INITIALIZE OBJECT
    def __init__(_self):
        super().__init__()

        # window settings
        _self.geometry('800x400')
        _self.title('Hegewald GmbH')
        _self.resizable(False, False)

        # create menu
        _self.create_menu()

        # create tab
        _self.create_notebook()

        # create frames
        _self.create_frame('Cyclovoltametrie', CONFIG['CYCLODATA'])
        _self.create_frame('Squarewave-Voltametrie', CONFIG['SQUAREWAVEDATA'])

        # create buttons
        _self.create_button(_self.start, 'start', 9, 0)
        _self.create_button(_self.stop, 'stop', 10, 0)
        _self.create_button(_self.clear, 'clear', 10, 1)

        # create graph
        _self.create_graph()



    # CREATE GUI ELEMENTS
    def create_menu(_self):
        _self.menu = MENU(_self)

    def create_notebook(_self, row=1, column=0):
        _self.notebook = ttk.Notebook(_self, name='tab')
        _self.notebook.bind('<<NotebookTabChanged>>', _self.tab_changed)
        _self.notebook.grid(row=row, column=column)

    def create_frame(_self, name, data=[]):
        _self.frames.append(FRAME(_self, _self.notebook, name, data))

    def create_button(_self, click, name, row, column):
        BUTTON(_self, click, name, row, column)

    def create_graph(_self):
        _self.graph = Graph(_self)



    # TAB EVENTS
    def tab_changed(_self, event):
        _self.active_tab = _self.notebook.index('current')
        _self.active_frame = _self.frames[_self.active_tab]

        if (_self.active_tab == 0):
            _self.frame_data = CONFIG['CYCLODATA']

        if (_self.active_tab == 1):
            _self.frame_data =  CONFIG['SQUAREWAVEDATA']

    # BUTTON EVENTS
    def start(_self):
        print('start') # start potentiostat 

    def stop(_self):
        print('stop') # stop potentiostat 

    def clear(_self):
        _self.clear_values()



    # HELPER
    def get_values(_self):
        data = {}

        for name in _self.frame_data:
            try:
                value = _self.active_frame.frame.__dict__[name].entry.get()

                if (not value):
                    raise ValueError

                data[name] = int(value)
            except ValueError:
                data[name] = 0

        return data

    def clear_values(_self):            
        for name in _self.frame_data:
            _self.active_frame.frame.__dict__[name].entry.delete(0, tk.END)
            _self.active_frame.frame.__dict__[name].label_error['text'] = ''
            _self.active_frame.frame.__dict__[name].entry['foreground'] = 'black'