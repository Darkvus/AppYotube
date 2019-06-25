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
        self.raiz = Tk()
        self.raiz.title("Descargar Youtube")
        self.menu = Menu(self.raiz)
        self.raiz.config(menu=self.menu)
        #Variables
        self.url = StringVar()
        self.ini = IntVar(value=1)
        self.fin = IntVar(value=10)
        self.ruta = StringVar()
        
        #Labels
        self.urlLabel = Label(self.raiz, text="URL Playlist o Video:")
        self.urlText = Entry(self.raiz, textvariable=self.url, width=10) 
        self.rutaLabel = Label(self.raiz, text="Directorio:")
        self.rutaText = Entry(self.raiz, textvariable=self.ruta, width=10) 
    	self.iniLabel = Label(self.raiz, text="Inicio Playlist:")
        self.iniText = Entry(self.raiz, textvariable=self.ini, width=10) 
        self.finLabel = Label(self.raiz, text="Fin Playlist:")
        self.finText = Entry(self.raiz, textvariable=self.fin, width=10)

        #Botones
        self.donwload = Button(self.raiz, text="Descargar", command=partial(downAudio, self))
        self.salir = Button(self.raiz, text="Salir", command=sys.exit)
        self.rutaButton = Button(self.raiz, text=" ", command=self.selector)
        
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
        self.raiz.mainloop()

    def selector(self):
        ruta = tkFileDialog.askdirectory()
        self.rutaText.insert(0,ruta)
    

def hi(self):
    print('HOLA SOY FUNCION FUERA DE LA CLASE: '+ str(self.url.get()))

def main():
    mi_app = YouTube()
    return 0


