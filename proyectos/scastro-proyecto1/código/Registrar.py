import sys
from tkinter import*

def Menu1 ():
    
    def Registrar():
        mtext = ment.get ()
        mlabel2 = Label (mGui, text = mtext).pack ()
        return


        mGui = Tk ()
        ment = StringVar ()

        mGui.geometry ('700x700+450+150')
        mGui.title ('')

        Letra_txt = PhotoImage (file = "registrar.png")

        mlabel = Label (mGui, image = Letra_txt). pack ()

        mEntry = Entry (width = 50, justify = CENTER).pack()

        Button (mGui, text = 'Ok', command = Registrar,fg = 'black', bg = 'grey' ).pack ()


import json        
