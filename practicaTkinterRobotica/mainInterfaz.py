import lib.vrep as vrep 
import tkinter
from tkinter import * 
from tkinter.messagebox import * # Para showinfo, etc  

root = tkinter.Tk() 

def conectarSimulador(): 
    global root, stringEstado, clientID, botonCapturar, botonDesconectar, estaSimulacionDetenida
    vrep.simxFinish(-1)
    clientID = vrep.simStart('127.0.0.1', 19999, True, True, 5000, 5)

    if clientID != -1: 
        showinfo("Práctica PTC Tkinter Robótica", "Conexión con VREP establecida")
        stringEstado.set("Conectado a VREP")
        estaSimulacionDetenida = False 
        botonCapturar['state'] = 'normal'
        botonDesconectar['state'] = 'normal'
    else: 
        showerror("Práctica PTC Tkinter Robótica", "Debe iniciar el simulador")

def funcionalidadCapturar(): 
    return 1 

# Inicializamos tkinter  
root.geometry("700x300")
root.title("Práctica PTC Tkinter Robótica")
stringEstado = StringVar() 
stringEstado.set("No conectado a VREP")
botonCapturar = Button(root, text="Capturar", command=funcionalidadCapturar, state=DISABLED)
botonDesconectar = Button(root, text="Detener y desconectar VREP")
estaSimulacionDetenida = True

# Columna 1
etiquetaAdvertencia = Label(root, text="Es necesario ejecutar el simulador VREP")
botonConectar = Button(root, text="Conectar con VREP", command=conectarSimulador)

root.mainloop() 
