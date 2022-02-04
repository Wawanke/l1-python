# Créé par christinefrodeau, le 24/11/2021 en Python 3.7

import tkinter as tk
#3.Cible en couleur

#ordre les couleurs sont blue, green, black, yellow, magenta, red

CANVAS_WIDTH, CANVAS_HEIGHT = 1100, 600

tab_couleur = ["blue", "green", "black", "yellow", "magenta", "red"]

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="white")
    k = 0
    tl = 0
    nb = int(input("Nombres de cercles : "))
    for i in range(nb):
        x1 = 549 - k
        y1 = 299 - k
        x2 = 551 + k
        y2 = 301 + k
        k += 5
        tl += 1
        if tl == len(tab_couleur) - 1 :
            tl = 0
        color = tab_couleur[tl]
        canvas.create_oval(x1, y1, x2, y2, width = 5, outline = color)

    canvas.pack()
    root.mainloop()
    print(color, tab_couleur)