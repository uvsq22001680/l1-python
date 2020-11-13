def bisextile(jour):
    annee = 2020
    while jour >= 0:
        if annee % 4 == 0 and ( annee %100 != 0 or annee %400 != 0 ):
            print(annee, "est bisextile")
            jour -= 366
        else:
            jour -= 365
        annee += 1