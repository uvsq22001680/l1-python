##auteurs:Gaetan bres 
##groupe TD: MIASHS TD 2

#################
#import des librairies 
import tkinter as tk

#####################
#constantes
COULEUR_FOND="grey180"
LARGEUR=600
HAUTEUR=400
#####################
#fonctions
def quadrillage():
    """Affiche un quadrillage"""
    pass

######################
#programme principal 
racine=tk.Tk()
racine.title("jeu de la vie")
#creation de widgets 
canvas=tk.Canvas(racine,bg=COULEUR_FOND,width=LARGEUR,height=HAUTEUR)
quadrillage()
#placement de widgets
canvas.grid(row=0)
#boucle principal
racine.mainloop