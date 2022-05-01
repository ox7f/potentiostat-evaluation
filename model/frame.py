from tkinter import Frame
from model.entry import ENTRY

class FRAME:
    def __init__(_self, root, tab=None, text='', data=[]):
        super().__init__()
 
        _self.frame = Frame(tab)
        tab.add(_self.frame, text=text)

        # create entries
        for index, name in enumerate(data):
            _self.frame.__dict__[name] = ENTRY(root, _self.frame, name, index)
