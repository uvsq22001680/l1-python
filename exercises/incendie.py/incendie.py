##auteurs:Gaetan bres 
##groupe TD: MIASHS TD 2

#################
#import des librairies 
import tkinter as tk

#### import random
import random as rd
####### definition des variables globales
 
#####################
#definition des constantes
LARGEUR=600
HAUTEUR=400
TAILLE_C=20

#####################
#definition des fonctions
def quadrillage() :
    '''construit un quadrillage'''
    xl=0
    for i in range(4): #60*10=600
        canvas.create_line(xl, 0, xl,LARGEUR, fill ='black')
        canvas.create_line(0, xl,LARGEUR, xl, fill ='black')
        xl=xl+TAILLE_C

def tableau_base() :
    global T
    T = []
    L = []
    for i in range(60) :#initialisation du tableau à 2 dimensions
        T.append(L) 
        for j in range(60):
            if i == 0 or i == 60-1 or j == 0 or j == 60-1:
                L.append(0) #on remplit les bords de vides
            else :
                L.append(randint(0,1)) #On place aléatoirement des arbres ou du vide
        L = []
    return T

def lancement():
    quadrillage()
    tableau_base()

    

######################
#programme principal 
racine=tk.Tk()
racine.title("incendie")
#creation de widgets 
canvas=tk.Canvas(racine,bg="white",width=LARGEUR,height=HAUTEUR)
quadrillage()
#placement de widgets
canvas.grid()
#liaison des evenements

#boucle principal
racine.mainloop()
