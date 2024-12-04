from tkinter import *
from tkinter import ttk
import numpy as np

# Mendefinisikan variabel global
resolutionX = 0
resolutionY = 0
mapArr = np.zeros((1, 1))

def showRes(mapArr):
    Label(interface, text=mapArr).grid(row=5, column=0)

def errorMsg(message):
    Label(interface, text=message).grid(row=5, column=0)

def resInputHandler():
    if(int(resXInput.get()) > 5 and int(resYInput.get()) > 5):
        resolutionX = int(resXInput.get())
        resolutionY = int(resYInput.get())
        mapArr = np.zeros((resolutionX, resolutionY))
        showRes(mapArr)
    else:
        errorMsg("Harus > 5")


# Membuat objek antarmuka
interface = Tk()
interface.title("BFS Random Map Generator")
interface.geometry("400x400")
interface.iconbitmap("assets/icon.ico")

Label(interface, text="Resolusi X: ").grid(row=1, column=0)
resXInput = Entry(interface, width=10)
resXInput.grid(row=1, column=1)
Label(interface, text="Resolusi Y: ").grid(row=2, column=0)
resYInput = Entry(interface, width=10)
resYInput.grid(row=2, column=1)
Button(interface, text="OK", command=resInputHandler).grid(row=3, column=1)

interface.mainloop()