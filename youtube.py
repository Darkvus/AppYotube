"""
	This script downloading music or video of youtube
"""
import sys
import os
from functools import partial
if sys.version_info.major == 2:
    import Tkinter, Tkconstants, tkFileDialog
    from Tkinter import *
elif version_info.major == 3:
    from tkinter import Tk, filedialog
    from tkinter import *

from utils import downAudio


class YouTube():
    def __init__(self):
        #Ventana
        
        #Variables
       
        #Labels
        

        #Botones
        
        
        #Packs
        self.urlLabel.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.urlText.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.rutaLabel.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        self.rutaText.pack(side=LEFT, fill=BOTH, expand=False, padx=10, pady=5)
        self.rutaButton.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.iniLabel.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.iniText.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.finLabel.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.finText.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
        self.donwload.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        self.salir.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)  

        #Inicio Ventana
       

    def selector(self):
        ruta = tkFileDialog.askdirectory()
        self.rutaText.insert(0,ruta)
    

def hi(self):
    print('HOLA SOY FUNCION FUERA DE LA CLASE: '+ str(self.url.get()))

def main():
    mi_app = YouTube()
    return 0


