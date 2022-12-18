import lib.vrep as vrep 
import tkinter
from tkinter import * 
from tkinter.messagebox import * # Para showinfo, etc  

# Valores por defecto 
valorIteraciones = 0
valorCerca = 0
valorMedia = 0
valorLejos = 0
valorMinPuntos = 0
valorMaxPuntos = 0
valorUmbralDistancia = 0
valorCambiar = 0

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

def funcionalidadPredecir (): 
    return True 

def funcionalidadSalir (): 
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
botonConectar = Button(root, text="Conectar con VREP", command=funcionalidadConectar)
botonDesconectar = Button(root, text="Detener y Desconectar VREP", command=funcionalidadDesconectar)
botonSalir = Button(root, text="Salir", command=funcionalidadSalir)

# Botones apartados 
botonCapturar = Button(root, text="Capturar", command=funcionalidadCapturar, state=DISABLED)
botonAgrupar = Button(root, text="Agrupar", command=funcionalidadAgrupar, state=DISABLED)
botonCaracteristicas = Button(root, text="Extraer caracteristicas", command=funcionalidadCaracteristicas, state=DISABLED)
botonClasificador = Button(root, text="Entrenar clasificador", command=funcionalidadClasificador)
botonPredecir = Button(root, text="Predecir", command=funcionalidadPredecir, state=DISABLED)

# Etiquetas parámetros 
etiquetaParametros = Label(root, text="Parámetros")
etiquetaIteraciones = Label(root, text="Iteraciones: ")
etiquetaCerca = Label(root, text="Cerca:")
etiquetaMedia = Label(root, text="Media:")
etiquetaLejos = Label(root, text="Lejos:")
etiquetaMinPuntos = Label(root, text="MinPuntos:")
etiquetaMaxPuntos = Label(root, text="MaxPuntos:")
etiquetaUmbralDistancia = Label(root, text="UmbralDistancia:")
etiquetaCambiar = Label(root, text="Cambiar:")

# Cajas de respuesta 
cajaIteraciones = Entry(root, width=5)
cajaIteraciones.insert(0, valorIteraciones)
cajaCerca = Entry(root, width=5)
cajaCerca.insert(0, valorCerca)
cajaMedia = Entry(root, width=5)
cajaMedia.insert(0, valorMedia)
cajaLejos = Entry(root, width=5)
cajaLejos.insert(0, valorLejos)
cajaMinPuntos = Entry(root, width=5)
cajaMinPuntos.insert(0, valorMinPuntos)
cajaMaxPuntos = Entry(root, width=5)
cajaMaxPuntos.insert(0, valorMaxPuntos)
cajaUmbralDistancia = Entry(root, width=5)
cajaUmbralDistancia.insert(0, valorUmbralDistancia)
cajaCambiar = Entry(root, width=5)
cajaCambiar.insert(0, valorCambiar)

# Ficheros 
etiquetaFicheros = Label(root, text="Ficheros para la captura")
cajaListaFicheros = Listbox(root, width=35, height=12)

listaFicheros = [
    "positivo1/enPieCerca.json", 
    "positivo2/enPieMedia.json", 
    "positivo3/enPieLejos.json", 
    "positivo4/sentadoCerca.json", 
    "positivo5/sentadoMedia.json", 
    "positivo6/sentadoLejos.json", 
    "negativo1/cilindroMenorCerca.json",
    "negativo2/cilindroMenorMedia.json",
    "negativo3/cilindroMenorLejos.json",
    "negativo4/cilindroMayorCerca.json",
    "negativo5/cilindroMayorMedia.json", 
    "negativo6/cilindroMayorLejos.json",   
    ]

for fichero in listaFicheros: 
    cajaListaFicheros.insert(tkinter.END, fichero) 

# Columna 0
etiquetaAdvertencia.grid(row=0, column=0)
botonConectar.grid(row=, column=0)
botonDesconectar.grid(row=, column=0)
stringEstado.grid(row=, column=0)
botonCapturar.grid(row=, column=0)
botonAgrupar.grid(row=, column=0)
botonCaracteristicas.grid(row=, column=0)
botonClasificador.grid(row=, column=0)
.grid(row=, column=0)
.grid(row=, column=0)

# Columna 1 
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)
.grid(row=, column=1)

# Columna 2 
.grid(row=, column=2)
.grid(row=, column=2)
.grid(row=, column=2)
.grid(row=, column=2)
.grid(row=, column=2)
.grid(row=, column=2)
.grid(row=, column=2)

# Columna 3 
.grid(row=, column=3)
.grid(row=, column=3, rowspan=6)

root.mainloop() 
