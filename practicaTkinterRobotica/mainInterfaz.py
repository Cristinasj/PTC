import tkinter
from tkinter import * 

root = tkinter.Tk() 

# Inicializamos tkinter  
def main(): 
    global root 
    root.geometry("700x300")
    root.title("Práctica PTC Tkinter Robótica")

    # Columna 1
    advertencia = Label(root, text="Es necesario ejecutar el simulador VREP")

    root.mainloop() 

main()   