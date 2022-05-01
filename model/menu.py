from config import CONFIG

from lib.utils import save_file, open_file, get_ports
from tkinter import Menu

class MENU:
    ports = []
    port = ''

    def __init__(_self, root=None):
        _self.root = root
        _self.menu = Menu(root)
        root.config(menu=_self.menu)

        _self.ports = ['COM1', 'COM2', 'COM3', 'USB1'] #get_ports()

        _self.create_file_menu()
        _self.create_interface_menu()

    def create_file_menu(_self):
        _self.file = Menu(_self.menu, tearoff=0)

        _self.file.add_command(label='Open',command=open_file)
        _self.file.add_command(label='Save',command=save_file)
        _self.file.add_separator()
        _self.file.add_command(label='Exit',command=quit)

        _self.menu.add_cascade(label='File', menu=_self.file)

    def create_interface_menu(_self):
        _self.interface = Menu(_self.menu, tearoff=0)

        for port in _self.ports:
            _self.interface.add_radiobutton(label=port, command=lambda arg0=port: _self.select_port(arg0))

        _self.menu.add_cascade(label='Interface', menu=_self.interface)

    def select_port(_self, port):
        _self.select_port = port


