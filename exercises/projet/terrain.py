##auteurs:Gaetan bres 
##groupe TD: MIASHS TD 2

#################
#import des librairies 
import tkinter as tk


####### definition des variables globales
 
#####################
#definition des constantes
LARGEUR=int(input('Choisir largeur'))
TAILLE_C=LARGEUR//50

#####################
#definition des fonctions
def quadrillage() :
    '''construit un quadrillage'''
    xl=0
    for i in range(50):
        canvas.create_line(xl, 0, xl,LARGEUR, fill ='black')
        canvas.create_line(0, xl,LARGEUR, xl, fill ='black')
        xl+=TAILLE_C

    

######################
#programme principal 
racine=tk.Tk()
racine.title("terrain")
#creation de  widgets 
canvas=tk.Canvas(racine,bg="white",width=LARGEUR,height=HAUTEUR)
quadrillage()
#placement de widgets
canvas.grid()
#liaison des evenements

#boucle principal
racine.mainloop()

