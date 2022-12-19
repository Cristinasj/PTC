import lib.vrep as vrep 
import tkinter
from tkinter import * 
from tkinter.messagebox import * # Para showinfo, etc  
import os 
import capturar

# Valores por defecto 
valoresPorDefecto = {
    "Iteraciones": 0, 
    "Cerca": 0, 
    "Media": 0, 
    "Lejos": 0, 
    "MinPuntos": 0, 
    "MaxPuntos": 0, 
    "UmbralDistancia": 0, 
    "Cambiar": 0
}

# Constantes 
headerPTC = "Práctica PTC Tkinter Robótica"

def funcionalidadConectar(): 
    global root, IDcliente, stringEstado, botonCapturar, botonDesconectar, estaSimulacionDetenida
    vrep.simxFinish(-1)
    IDcliente = vrep.simStart('127.0.0.1', 19999, True, True, 5000, 5)

    if IDcliente != -1: 
        showinfo(headerPTC, "Conexión con VREP establecida")
        stringEstado.set("Conectado a VREP")
        estaSimulacionDetenida = False 
        botonCapturar['state'] = 'normal'
        botonDesconectar['state'] = 'normal'
    else: 
        showerror(headerPTC, "Debe iniciar el simulador")

def funcionalidadCapturar(): 
    global cajaListaFicheros, IDcliente

    if cajaListaFicheros.curselection(): 
        ficheroElegido = cajaListaFicheros.get(cajaListaFicheros.curselection()[0])

        if not os.path.isfile(ficheroElegido): 
            pregunta = "Se va a crear el fichero:\n" 
            pregunta += ficheroElegido
            pregunta += "¿Está seguro?" 
        else: 
            pregunta = "El fichero: " 
            pregunta += ficheroElegido 
            pregunta += " Ya existe. Se creará de nuevo. ¿Está seguro?"
        haDichoSi = askyesno(headerPTC, pregunta)

        if haDichoSi: 
            capturar.funcionalidad(IDcliente, ficheroElegido, valoresPorDefecto)

        botonAgrupar["state"] = "normal"

def funcionalidadDesconectar (): 
    return True 

def funcionalidadAgrupar (): 
    global botonExtraer 
    botonExtraer["state"] = "normal"

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
root.title(headerPTC)

# Variables necesarias para GUI 
stringEstado = StringVar() 
stringEstado.set("No conectado a VREP")
estaSimulacionDetenida = True
etiquetaAdvertencia = Label(root, text="Es necesario ejecutar el simulador VREP")
etiquetaEstado = Label(root, textvariable=stringEstado)

# Botones ON OFF 
botonConectar = Button(root, text="Conectar con VREP", command=funcionalidadConectar)
botonDesconectar = Button(root, text="Detener y Desconectar VREP", command=funcionalidadDesconectar)
botonSalir = Button(root, text="Salir", command=funcionalidadSalir)

# Botones apartados 
botonCapturar = Button(root, text="Capturar", command=funcionalidadCapturar, state=DISABLED)
botonAgrupar = Button(root, text="Agrupar", command=funcionalidadAgrupar, state=DISABLED)
botonCaracteristicas = Button(root, text="Extraer caracteristicas", command=funcionalidadCaracteristicas, state=DISABLED)
botonClasificador = Button(root, text="Entrenar clasificador", command=funcionalidadClasificador, state=DISABLED)
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
cajaIteraciones.insert(0, valoresPorDefecto["Iteraciones"])
cajaCerca = Entry(root, width=5)
cajaCerca.insert(0, valoresPorDefecto["Cerca"])
cajaMedia = Entry(root, width=5)
cajaMedia.insert(0, valoresPorDefecto["Media"])
cajaLejos = Entry(root, width=5)
cajaLejos.insert(0, valoresPorDefecto["Lejos"])
cajaMinPuntos = Entry(root, width=5)
cajaMinPuntos.insert(0, valoresPorDefecto["MinPuntos"])
cajaMaxPuntos = Entry(root, width=5)
cajaMaxPuntos.insert(0, valoresPorDefecto["MaxPuntos"])
cajaUmbralDistancia = Entry(root, width=5)
cajaUmbralDistancia.insert(0, valoresPorDefecto["UmbralDistancia"])
cajaCambiar = Entry(root, width=5)
cajaCambiar.insert(0, valoresPorDefecto["Cambiar"])

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
botonConectar.grid(row=1, column=0)
botonDesconectar.grid(row=2, column=0)
etiquetaEstado.grid(row=3, column=0)
botonCapturar.grid(row=4, column=0)
botonAgrupar.grid(row=5, column=0)
botonCaracteristicas.grid(row=6, column=0)
botonClasificador.grid(row=7, column=0)
botonPredecir.grid(row=8, column=0)
botonSalir.grid(row=9, column=0)

# Columna 1 
etiquetaParametros.grid(row=1, column=1)
etiquetaIteraciones.grid(row=2, column=1)
etiquetaCerca.grid(row=3, column=1)
etiquetaMedia.grid(row=4, column=1)
etiquetaLejos.grid(row=5, column=1)
etiquetaMinPuntos.grid(row=6, column=1)
etiquetaMaxPuntos.grid(row=7, column=1)
etiquetaUmbralDistancia.grid(row=8, column=1)
etiquetaCambiar.grid(row=9, column=1)

# Columna 2 
cajaIteraciones.grid(row=2, column=2)
cajaCerca.grid(row=3, column=2)
cajaMedia.grid(row=4, column=2)
cajaLejos.grid(row=5, column=2)
cajaMinPuntos.grid(row=6, column=2)
cajaMaxPuntos.grid(row=7, column=2)
cajaUmbralDistancia.grid(row=8, column=2)

# Columna 3 
etiquetaFicheros.grid(row=1, column=3)
cajaListaFicheros.grid(row=3, column=3, rowspan=6)

root.mainloop() 
