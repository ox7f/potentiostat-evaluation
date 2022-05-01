from config import CONFIG
from tkinter import filedialog
import serial.tools.list_ports

# HELPER
def get_ports(_self):
    return [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]

# FILE HELPER
# TODO: only accept '.txt'
def open_file(_self):
    filepath = filedialog.askopenfilename()
    print('open file', filepath)

    if filepath:
        file = open(filepath, 'r')
        print(file.read())
        file.close()

def save_file(_self):
    print('TODO: save file')