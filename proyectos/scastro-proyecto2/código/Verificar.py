import sys
from tkinter import*
import json

def Menu2 ():
    
    def Verificar():
        mtext = ment.get ()
        mlabel2 = Label (mGui, text = mtext).pack ()
        return

    mGui = Tk ()
    ment = StringVar ()

    mGui.geometry ('500x500+450+150')
    mGui.title ('')

    Letra_txt = PhotoImage (file = "verificar.png")

    mlabel = Label (mGui, image = Letra_txt). pack ()

    mEntry = Entry (width = 50, justify = CENTER).pack()

    Button (mGui, text = 'Ok', command = Verificar,fg = 'black', bg = 'grey' ).pack ()

