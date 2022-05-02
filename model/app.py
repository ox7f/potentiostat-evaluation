from config import CONFIG

# von ordner 'model' importiere datei 'frame'
from model.frame import FRAME
from model.button import BUTTON
from model.graph import Graph
from model.menu import MENU

import tkinter as tk
import tkinter.ttk as ttk

# tk => module
# tk.TK => klasse
class App(tk.Tk): #Erstellung der Klasse App und Vererbung von tkinter Klasse
    #Variablen werden direkt beim Start erstellt und nicht erst beim Aufruf der jeweiligen Funktion, sofort im Fenster sichtbar!
    menu = None #Erstellung der Variable Menu
    frames = [] #um mehrere Frames in einer Variable zu speichern
    frame_data = [] #Sind die Daten von CYCLODATA ODER SQUAREWAVEDATA (config), je nach dem welcher Tab gerade Aktiv ist
    active_frame = None #ausgewaehlter frame (frame.py), entweder Cyclo oder Squarewave dort sind alle Eingabeboxen mit ihren Wert
    data = [] # Um alle Werte von der Messung in eine Datei zu speichern; 

    # INITIALIZE OBJECT
    def __init__(_self): #Konstruktor -> erstellt dann das Objekt, also das Fenster mit den jeweiligen Widgets 
        super().__init__() #-> Erben von tk.Tk(Elternklasse) um dann z.B. geometry, title usw. auszuwählen

        # window settings
        _self.geometry('800x400') #Größe des Fensters
        _self.title('Hegewald GmbH') #Titel des Fensters
        _self.resizable(False, False) #Größe des Fensters nicht veränderbar

        # create menu
        _self.create_menu()
        #über alle _self, weil es (zur klasse gehoert)
        # create tab
        _self.create_notebook() #Die Methode zur Erstellung der Tableiste, wo beide Tabs später rein kommen

        # create frames
        _self.create_frame('Cyclovoltametrie', CONFIG['CYCLODATA']) # _self.frames[0]
        _self.create_frame('Squarewave-Voltametrie', CONFIG['SQUAREWAVEDATA'])  #_self.frames[1]

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
        frame = FRAME(_self, _self.notebook, name, data) #Erstellung eines Frame Objektes(frame.py), speicherung in Frame
        _self.frames.append(frame) #Erstelltes Frame Objekt der Liste hinzufuegen

    def create_button(_self, click, name, row, column):
        BUTTON(_self, click, name, row, column)

    def create_graph(_self):
        _self.graph = Graph(_self)


    # TAB EVENTS
    def tab_changed(_self, event):
        active_tab = _self.notebook.index('current') #In a call to the Notebook widget's .index() method, use the string "end" to determine the current number of tabs displayed.
        _self.active_frame = _self.frames[active_tab] #hole Frame aus liste (index 0 oder 1) (man schaut und holt)

        if (active_tab == 0):
            _self.frame_data = CONFIG['CYCLODATA']

        if (active_tab == 1):
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