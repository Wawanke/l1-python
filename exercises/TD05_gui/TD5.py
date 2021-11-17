# Créé par christinefrodeau, le 29/10/2021 en Python 3.7
#import tkinter as tk
import tkinter as tk
import random
from random import randint
#Notes importantes

#Bitmap sert à titrer des widgets de "paramètres" tel que ex. : aide, infos, déconnexion

#1. Prise en main
"""
from tkinter import *

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

if __name__ == '__main__':
    root = Tk()

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)
    #Fait de façon horizontal

    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
    canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

    #Fait de façon verticale

    x = CANVAS_WIDTH / 2
    y1 = 100
    y0 = CANVAS_HEIGHT - 100
    canvas.create_line(x, y0, x, y1)
    canvas.create_oval(x - 50, y0 + 50, x + 50, y0 - 50)
    canvas.create_oval(x - 50, y1 + 50, x + 50, y1 - 50)
    #canvas.create_oval(x - 50, (y0 + y1) / 2 + 50, x - 50, (y0 + y1) + 50)
    #canvas.create_oval(x - 50, (y0 + y1) / 2 + 50, x - 50, (y0 + y1) + 50)
    canvas.create_oval(x - 50, (y0 + y1) / 2 + 50, x + 50, (y0 + y1) / 2 - 50)
    # Fin de votre code

    canvas.pack()
    root.mainloop()
"""

#2. Dessins aléatoires



CANVAS_WIDTH, CANVAS_HEIGHT = 1100, 600

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="black")

    #Fonction cercle bleu avec position aléatoire
    def cercle():
        x1, y1 = random.randint(0, 1000), random.randint(0, 500)
        x2, y2 = x1 + 100, y1 + 100
        canvas.create_oval(x1, y1, x2, y2, outline = "red")
    def carre():
        pass #Créer le carré (s'inspirer du cercle au-dessus)


    #canvas.canvas_tk

    bouton = tk.Button(root, text="Choisir une couleur", activebackground = "green", borderwidth = 8, font = ("helvetica", "30"), overrelief = "sunken")
    bouton.grid(row = 0,column = 2)
    bouton = tk.Button(root, text="Cercle", command = cercle(), font = ("helvetica", "30"))
    bouton.grid(row = 1,column = 0)
    bouton = tk.Button(root, text="Carré", command = carre(), font = ("helvetica", "30"))
    bouton.grid(row = 2,column = 0)
    bouton = tk.Button(root, text="Croix", font = ("helvetica", "30"))
    bouton.grid(row = 3,column = 0)
    # Affichage

    canvas.grid(row=1,column=1,rowspan=3,columnspan=3)
    root.mainloop()



#3.Cible en couleur

#ordre les couleurs sont blue, green, black, yellow, magenta, red

"""
def cercle_color(x1, x2, y1, y2, color):
    root = Tk()
    canvas = Canvas(root, width = 1000, height = 800)

    canvas.create_oval(x1, y1, x2, y2)

    canvas.pack()
    root.mainloop()


cercle_color(50, 50, 100, 100, "blue")
"""
