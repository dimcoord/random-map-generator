from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw
import numpy as np
import random as rand
import os

res_x = int(0)
res_y = int(0)
h_max = int(0)
b_max = int(0)
m_max = int(0)
map_name = str("")
map_array = np.zeros((res_y, res_x), dtype=int)
icon = "assets/icon.ico"
save_folder = "results"
bgcolor = "#031273"

def errorMsg(message, row, col):
    Label(interface, text=message, fg="white", bg="red").grid(row=row, column=col)

def inputHandler():
    error = False
    if (map_name_input.get() != ""):
        map_name = str(map_name_input.get())
    else:
        map_name = "Randomly Generated Map"
    if (int(h_max_input.get()) > 1):
        h_max = int(h_max_input.get())
    else:
        errorMsg("ERROR: Ketinggian harus > 1", 7, 1)
        error = True
    if (int(b_max_input.get()) > 0):
        b_max = int(b_max_input.get())
    else:
        errorMsg("ERROR: Ketebalan harus > 0", 8, 1)
        error = True
    if (int(m_max_input.get()) > 5):
        m_max = int(m_max_input.get())
    else:
        errorMsg("ERROR: Cabang harus > 5", 9, 1)
        error = True
    if((100 <= int(res_x_input.get()) <= 2000) and (100 <= int(res_y_input.get()) <= 2000)):
        res_x = int(res_x_input.get())
        res_y = int(res_y_input.get())
        map_array = np.zeros((res_y, res_x), dtype=int)
        if (not error):
            # mapWindow(map_name, map_array)
            randomizeVertices(h_max, m_max, map_array)
            drawMap(res_x, res_y, h_max, b_max, map_array, map_name)
    else:
        errorMsg("ERROR: Resolusi harus 100-2000", 10, 1)

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

# Randomize vertices using random (skip adjacent range of vertices)
def randomizeVertices(h_max, m_max, map_array):
    selected = []
    for i in range(20, map_array.shape[0]-20):
        for j in range(20, map_array.shape[1]-20):
            if all(abs(i - x) > 1 or abs(j - y) > 1 for x, y in selected):
                selected.append((i, j))
                map_array[i, j] = rand.choice([0, h_max])

# Static drawing method using PIL
def drawMap(res_x, res_y, h_max, b_max, map_array, map_name):
    img = Image.new("RGB", (res_x, res_y), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(map_array.shape[0]):
        for j in range(map_array.shape[1]):
            if(map_array[i, j] == 1):
                draw.point((i, j), fill="green")
            elif(map_array[i, j] == 2):
                draw.point((i, j), fill="yellow")
            elif(map_array[i, j] == 3):
                draw.point((i, j), fill="orange")
            elif(map_array[i, j] == 4):
                draw.point((i, j), fill="red")
            else:
                draw.point((i, j), fill="blue")
    # img.resize((res_x*3, res_y*3), Image.NEAREST)

    # Create folder if it does not exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    img.save(os.path.join(save_folder, f"{map_name}.jpg"))

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

Label(interface, text="Ketinggian: ").grid(row=4, column=0)
h_max_input = Entry(interface, width=30)
h_max_input.grid(row=4, column=1)

Label(interface, text="Ketebalan: ").grid(row=5, column=0)
b_max_input = Entry(interface, width=30)
b_max_input.grid(row=5, column=1)

Label(interface, text="Cabang: ").grid(row=6, column=0)
m_max_input = Entry(interface, width=30)
m_max_input.grid(row=6, column=1)

Button(interface, text="OK", command=inputHandler).grid(row=3, column=2)




# TKInter main loop
interface.mainloop()