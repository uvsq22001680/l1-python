import tkinter as tk
racine=tk.Tk()

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400


    # Début de votre code
canvas=tk.Canvas(racine,height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
    
canvas.create_line(x0, y, x1, y)
canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

racine.mainloop()
