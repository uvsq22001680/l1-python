import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
COMPTEUR=0

###################
# Fonctions

def creer_balle():
    """Dessine un rond bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)

def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1] and canvas.itemconfigure(trait,0(HAUTEUR//2)+1,LARGEUR,(HAUTEUR//2)+1)
    if y0 <= 200 or y1 >= 400:
        balle[2] = -balle[2]
    if y0<=200:
        canvas.itemconfigure(trait,0,(HAUTEUR//2)+50,LARGEUR,(HAUTEUR//2)+50)

def creer_trait():
    global trait 
    trait=canvas.create_line(0,HAUTEUR//2,LARGEUR,HAUTEUR//2, fill='white')

for i in range(30):
    rebond()
    COMPTEUR+=1
if COMPTEUR<30:
    after.cancel(mouvement)

######################
# programme principal

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=600, height=400)
canvas.grid()
creer_trait()
balle = creer_balle()
mouvement()
racine.mainloop()
