from config import CONFIG
from tkinter import filedialog
import serial.tools.list_ports

# HELPER
def get_ports():
    return [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]

# FILE HELPER
def open_file():
    filepath = filedialog.askopenfilename()
    print('open file', filepath)

    if '.txt' in filepath:
        file = open(filepath, 'r')
        content = file.read()
        file.close()

        print(content)

def save_file():
    print('TODO: save file')