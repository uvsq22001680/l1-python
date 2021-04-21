##auteurs:Gaetan bres 
##groupe TD: MIASHS TD 2

#################
#import des librairies 
import tkinter as tk
#######variation globale
tableau= none 
#####################
#constantes
COULEUR_FOND = "grey100"
COULEUR_QUADR = "grey50"
COULEUR_VIVANT = "yellow"
LARGEUR = 600
LARGEUR = 600
HAUTEUR = 400
HAUTEUR = 400
# la longueur des carrés qui constituent le quadrillage
COTE = 10
NB_COL = LARGEUR // COTE
NB_LINE = HAUTEUR // COTE
#####################
#fonctions

def coord_to_lg(x, y):
    """Fonction qui retourne la colonne et la ligne du quadrillage
    à partir des coordonnées x et y"""
    return x // COTE, y // COTE

def change_carre(event):
    """Change l'état du carré sur lequel on a cliqué"""
    i, j = coord_to_lg(event.x, event.y)
    if tableau[i][j] == -1:
        x, y = i * COTE, j * COTE
        carre = canvas.create_rectangle(x, y, x + COTE,
                                        y + COTE, fill=COULEUR_VIVANT,
                                        outline=COULEUR_QUADR)
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = -1


def creer_tableau():
    """initialise un tableau à deux dimensions qui vaut -1 partout
    -1 est pour une case morte
    identifiant du carré dessiné si une case est vivante
    tableau[i][j] est la valeur de la case à la colonne i et la ligne j
    """
    global tableau
    tableau = []
    for i in range(NB_COL):
        tableau.append([-1] * NB_LINE)
    # tableau = [tableau_col for i in range(NB_COL)]

######################
#programme principal 
racine=tk.Tk()
racine.title("jeu de la vie")
#creation de widgets 
canvas=tk.Canvas(racine,bg=COULEUR_FOND,width=LARGEUR,height=HAUTEUR)
ligne_hor()
ligne_vert()
creer_tableau()
#placement de widgets
canvas.grid(row=0)
#liaison des evenements
canvas.bind("<Button-1>", change_carre)
#boucle principal
racine.mainloop