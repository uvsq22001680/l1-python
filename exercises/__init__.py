from tkinter import * 
racine = tk.Tk()
racine.title("Dessin aléatoire") 

choisir_couleur = tk.Button(racine, texte = "Choisir une couleur")
bouton_cercle = tk.Button(racine, texte = "Cercle")
bouton_croix = tk.Button(racine, texte = "Croix")
bouton_carré = tk.Button(racine, texte = "Carré")

choisir_couleur.grid(colum = 1, row = 0)
bouton_cercle.grid(colum = 0, row = 1)
bouton_croix.grid(colum = 0, row = 2)
bonton_carré.grid(colum = 0, row = 3)

canvas = Tk.Canvas(racine, width=500, hight=500, bg="black")
canvas.grid(colum = 1, row = 1, rowspan = 3)

racine.mainloop()

