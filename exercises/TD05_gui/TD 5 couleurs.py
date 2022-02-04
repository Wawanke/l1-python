# Créé par christinefrodeau, le 02/12/2021 en Python 3.7

import tkinter as tk
import random

CANVAS_WIDTH, CANVAS_HEIGHT = 1200, 600

if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg="white")


    def draw_pixel():

        for i in range(100):
            x = random.randint(0, 600)
            print(x)
            canvas.create_line(x, x, x+1, x, fill = "red")
    def ecran_aleatoire():
        pass
    def degrade_gris():
        pass
    def degrade_2D():
        pass

    bouton = tk.Button(root, text="Draw_pixel", command = draw_pixel, activebackground = "green", font = ("helvetica", "18"))
    bouton.grid(row = 0,column = 0)
    bouton = tk.Button(root, text="écran aléatoire", command = ecran_aleatoire, font = ("helvetica", "18"))
    bouton.grid(row = 0,column = 1)
    bouton = tk.Button(root, text="Degrade gris", command = degrade_gris, font = ("helvetica", "18"))
    bouton.grid(row = 0,column = 2)
    bouton = tk.Button(root, text="Degrade 2D", command = degrade_2D, font = ("helvetica", "18"))
    bouton.grid(row = 0,column = 3)
    # Affichage

    canvas.grid(row=1,column=1,columnspan=3)
    root.mainloop()

