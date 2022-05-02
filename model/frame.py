from tkinter import Frame
from model.entry import ENTRY

frame = Frame(root)
class FRAME:
    frame = None
    
    def __init__(_self, root, tab=None, text='', data=[]):
        super().__init__()
 
        _self.frame = Frame(tab) #erstelle tk frame
        tab.add(_self.frame, text=text) # konfiguriere tk frame (setze name)

        # create entries
        for index, name in enumerate(data): #schleife durch alle noetigen inputfelder 
            _self.frame.__dict__[name] = ENTRY(root, _self.frame, name, index) # erstelle inputfelder => speichern inputfelder im frame
            # _self.frame.__dict__ => verwandel klasse in liste