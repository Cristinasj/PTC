import lib.vrep as vrep 
import tkinter
from tkinter import * 
from tkinter.messagebox import * # Para showinfo, etc  


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

def funcionalidadConectar (): 
    return True 

def funcionalidadDesconectar (): 
    return True 

def funcionalidadAgrupar (): 
    return True 

def funcionalidadCaracteristicas (): 
    return True 

def funcionalidadClasificador (): 
    return True

# Inicialización tkinter  
root = tkinter.Tk() 
root.geometry("700x300")
root.title("Práctica PTC Tkinter Robótica")

# Variables necesarias para GUI 
stringEstado = StringVar() 
stringEstado.set("No conectado a VREP")
estaSimulacionDetenida = True
etiquetaAdvertencia = Label(root, text="Es necesario ejecutar el simulador VREP")

# Botones ON OFF 
botonDesconectar = Button(root, text="Detener y desconectar VREP")
botonConectar = Button(root, text="Conectar con VREP", command=funcionalidadConectar)

# Botones apartados 
botonCapturar = Button(root, text="Capturar", command=funcionalidadCapturar, state=DISABLED)
bottonDesconectar = Button(root, text="Detener y Desconectar VREP", command=funcionalidadDesconectar)
botonAgrupar = Button(root, text="Agrupar", command=funcionalidadAgrupar, state=DISABLED)
botonCaracteristicas = Button(root, text="Extraer caracteristicas", command=funcionalidadCaracteristicas, state=DISABLED)
botonClasificador = Button(root, text="Entrenar clasificador", command=funcionalidadClasificador)



# Columna 1


root.mainloop() 
