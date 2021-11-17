#Code de l'exemple
"""
from tkinter import *
import tkinter
import tkinter as tk
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
    canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    # Fin de votre code
    #Code de test
    canvas.create_bitmap(100, 300)

    top = tkinter.Tk()

    B1 = tkinter.Button(top, text ="error", relief=RAISED,\
                         bitmap="error")
    #B1.pack()

    filename = PhotoImage(file = "rainbow_cat.gif")
    image = canvas.create_image(500, 100, anchor=NE, image=filename)
    canvas.pack()
    root.mainloop()
"""

#Code pour un gif
"""
from tkinter import *
import os
import time
root = Tk()
c = Canvas(root,width = 500,height = 500)
c.pack()
frames = [PhotoImage(file=(os.path.expanduser("rainbow_cat.gif")),format = 'gif -index %i' % (i)) for i in range(2)]
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind >= 2:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
c.move(frames,0,-100)
root.update()
root.mainloop()







