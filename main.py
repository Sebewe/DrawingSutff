"""
This is a super simple program that will create a black square (if its inside the box)
I made it for a project that I decided to turn in a different direction but it's still fun to mess around with the drawing
feel free to use this for whatever you want I don't mind
"""
import tkinter as Tk
from threading import Thread

#constants/global variables... ALL CAPS = CONSTANT
OFFSET = 100
MULT_RATE = 9
IMG_SIZE = 28
grid = []
canvas = None
window = None

#initialize the frame and start it up, this runs in a seperate thread so that the other calcs don't have to wait on this
def createWindow(width, height, title):
    global grid
    for rows in range(IMG_SIZE):
        grid.append([])
        for cols in range(IMG_SIZE):
            grid[rows].append(0)

    global window
    window = Tk.Tk()
    window.geometry("{}x{}+200+100".format(width,height))
    window.title(string=title)

    global canvas
    canvas = Tk.Canvas(window, height=height, width=width)
    canvas.pack()
    canvas.create_rectangle(0,0, width, height, fill="white", outline="white")
    canvas.create_rectangle(OFFSET, OFFSET, OFFSET+(IMG_SIZE*MULT_RATE), OFFSET+(IMG_SIZE*MULT_RATE))
    canvas.focus_set()
    canvas.bind("<Button-1>", clicked)

    window.mainloop()

#what to do when clicked
def clicked(event):
    x, y = event.x - OFFSET, event.y - OFFSET
    xPos, yPos = int(x/MULT_RATE), int(y/MULT_RATE)
    if xPos < IMG_SIZE and xPos > -1 and yPos < IMG_SIZE and yPos > -1:
        grid[xPos][yPos] = 0 if grid[xPos][yPos] == 1 else 1
        canvas.create_rectangle(
            (xPos * MULT_RATE) + OFFSET,
            (yPos * MULT_RATE) + OFFSET,
            (xPos * MULT_RATE) + OFFSET + MULT_RATE,
            (yPos * MULT_RATE) + OFFSET + MULT_RATE,
            fill="white" if grid[xPos][yPos] == 0 else "black",
            outline="white" if grid[xPos][yPos] == 0 else "black"
        )
        canvas.create_rectangle(OFFSET, OFFSET, OFFSET+(IMG_SIZE*MULT_RATE), OFFSET+(IMG_SIZE*MULT_RATE), outline="black")

if __name__ == "__main__":
    thread = Thread(target=createWindow, args=(1000, 800, "Sebastian Modafferi"))
    thread.start()
