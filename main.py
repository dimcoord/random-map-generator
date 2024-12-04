from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw
import numpy as np

res_x = 0
res_y = 0
icon = "assets/icon.ico"
bgcolor = "#031273"

def showRes(map_array):
    Label(interface, text=map_array).grid(row=5, column=0)

def errorMsg(message, row, col):
    Label(interface, text=message, fg="white", bg="red").grid(row=row, column=col)

def inputHandler():
    if((50 <= int(res_x_input.get()) <= 100) and (50 <= int(res_y_input.get()) <= 50)):
        res_x = int(res_x_input.get())
        res_y = int(res_y_input.get())
        map_array = np.zeros((res_y, res_x), dtype=int)
        if (map_name_input.get() != ""):
            map_name = str(map_name_input.get()) 
        else:
            map_name = "Randomly Generated Map"
        # mapWindow(map_name, map_array)
        drawMap(res_x, res_y, map_array, map_name)
    else:
        errorMsg("ERROR: Resolusi harus 50-100", 5, 1)

# Interactive drawing method using Toplevel (Resource-intensive)
def mapWindow(map_name, map_array):
    map_interface = Toplevel(interface)
    map_interface.state("zoomed")
    map_interface.title(map_name)
    map_interface.iconbitmap(icon)
    # map_interface.configure(bg=bgcolor)
    for i in range(map_array.shape[0]):
        for j in range(map_array.shape[1]):
            Label(map_interface, text=str(map_array[i][j]), fg="white", bg=bgcolor).grid(row=i, column=j)

# Static drawing method using PIL
def drawMap(res_x, res_y, map_array, map_name):
    img = Image.new("RGB", (res_x, res_y), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(map_array.shape[0]):
        for j in range(map_array.shape[1]):
            if(map_array[i, j] != 0):
                draw.point((i, j), fill="black")
    img.show()
    img.save(f"{map_name}.jpg")

# Creating the interface
interface = Tk()
interface.title("BFS Random Map Generator")
interface.geometry("400x400")
interface.iconbitmap(icon)

# Varibles for the map
Label(interface, text="Nama Peta: ").grid(row=1, column=0)
map_name_input = Entry(interface, width=30)
map_name_input.grid(row=1, column=1)

Label(interface, text="Resolusi X: ").grid(row=2, column=0)
res_x_input = Entry(interface, width=30)
res_x_input.grid(row=2, column=1)

Label(interface, text="Resolusi Y: ").grid(row=3, column=0)
res_y_input = Entry(interface, width=30)
res_y_input.grid(row=3, column=1)

Button(interface, text="OK", command=inputHandler).grid(row=2, column=2)




# TKInter main loop
interface.mainloop()