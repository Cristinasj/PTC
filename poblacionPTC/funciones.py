# -*- coding: utf-8 -*-
import csv
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import matplotlib.pyplot as plt

def limpiaFichero(n):
    name = n+".csv"
    ficheroInicial=open(name,"r", encoding="utf8")
    cadenaPob=ficheroInicial.read()
    ficheroInicial.close()
    primero=cadenaPob.find("Total Nacional")
    ultimo=cadenaPob.find("Notas")
    cadenaFinal=cadenaPob[primero:ultimo]
    cabecera="Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010"
    name = n+"Final.csv"
    ficheroFinal=open(name, "w",encoding="utf8")
    ficheroFinal.write(cabecera+'\n'+cadenaFinal)
    ficheroFinal.close()
 
def readFich(n):
    name = n+".csv"
    with open(name, encoding="utf8") as csvarchivo:
        entrada = csv.reader(csvarchivo, delimiter=';')
        res = []
        for reg in entrada:
            if(reg[-1]):
                res.append(reg)
            else:
                res.append(reg[:-1])
    return res

def vabsYvrel(datos):
    d = [e[:9] for e in datos]
    d.pop(0)
    cabecera=["Provincia","2017","2016","2015","2014","2013","2012","2011","2017","2016","2015","2014","2013","2012","2011"]
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    desp = d.shape[1]-1
    res = np.zeros((d.shape[0],(desp)*2))
    for i in range(d.shape[1]-1):
        res[:,i] = d[:,i]-d[:,i+1]
        res[:,i+d.shape[1]-1] = (d[:,i]-d[:,i+1])/d[:,i+1]*100
    res = np.hstack((l,res))
    res = np.vstack((cabecera,res))
    return res

# =============================================================================
# Funcion para el ejercicio 4
# Como la funcion anterior calcula la variabilidad absoluta y relativa, pero en este
# caso tanto del total como por cada sexo
# Devuelve un numpy array con el resultado calculado
# =============================================================================
def vabsYvrelSex(datos):
    #Hago una copia para no modificar lo que nos pasan
    d = datos.copy()
        
    #Creo la nueva cabecera
    cabecera=["Comunidad","T2017","T2016","T2015","T2014","T2013","T2012","T2011","T2017","T2016","T2015","T2014","T2013","T2012","T2011"]
    cabecera.extend(["H2017","H2016","H2015","H2014","H2013","H2012","H2011","H2017","H2016","H2015","H2014","H2013","H2012","H2011"])
    cabecera.extend(["M2017","M2016","M2015","M2014","M2013","M2012","M2011","M2017","M2016","M2015","M2014","M2013","M2012","M2011"])
    #Elimino la cabecera
    d = d[1:,:]
    
    #Guardo todas las etiquetas y creo un np.array con todos los datos restantes
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    
    desp = 7
    #Creo en np.array que voy a devolver como resultado
    res = np.zeros((d.shape[0],desp*6))
    # Recorriendo unicamente los primeros 7 elementos que son lo que se corresponden
    # con los totales, calculo tanto éstos como por cada uno de los sexos y lo
    # añado al array resultado
    for i in range(desp):
        res[:,i] = d[:,i]-d[:,i+1]
        res[:,i+desp] = (d[:,i]-d[:,i+1])/d[:,i+1]*100
        
        res[:,i+desp*2] = d[:,i+desp+1]-d[:,i+desp+2]
        res[:,i+desp*3] = (d[:,i+desp+1]-d[:,i+desp+2])/d[:,i+desp+2]*100
        
        res[:,i+desp*4] = d[:,i+desp*2+2]-d[:,i+desp*2+3]
        res[:,i+desp*5] = (d[:,i+desp*2+2]-d[:,i+desp*2+3])/d[:,i+desp*2+3]*100
    
    #Añado la cabecera y las etiquetas
    res = np.hstack((l,res))
    res = np.vstack((cabecera,res))

    return res

# =============================================================================
# Funcion que crea un fichero css con el estilo que va a tener la tabla resultante
# =============================================================================
def createCSS():
    fileEstilo=open("resultados/estilo.css","w")

    estilo="""  table, th, td {
                    border-collapse: collapse;    
                    border:1px solid black;
                    font-family: Arial, Helvetica, sans-serif;
                    padding: 8px;
                    
                }  """
    
    fileEstilo.write(estilo)
    fileEstilo.close()

# =============================================================================
# Funcion que crea un HTM resultante con los datos que se le pasa como parámetro
# y haciendo unas determinadas tablas o graficas dependiendo del propio
# ejercicio para el que lo estemos ejecutando
# =============================================================================
def exportToHTML(data,fich,plot=None,ej1=False,ej2=False,ej3=False,ej4=False,ej5=False):
    name = fich+".htm"
    f = open(name,'w')

    if ej1:
        paginaPob = """<!DOCTYPE html><html>
        <head><title>Variabilidad Absoluta y relativa</title>
        <link rel="stylesheet" href="estilo.css">
        <meta charset="UTF-8"></head>
        <body><h1>Ej1-Variabilidad Absoluta y relativa</h1>"""
    elif ej2:
        paginaPob = """<!DOCTYPE html><html>
        <head><title>Valores por comunidades</title>
        <link rel="stylesheet" href="estilo.css">
        <meta charset="UTF-8"></head>
        <body><h1>Ej2- Valores por comunidades y sexos</h1>"""
    elif ej4:
        paginaPob = """<!DOCTYPE html><html>
        <head><title>Variabilidad Absoluta y relativa Comunidades</title>
        <link rel="stylesheet" href="estilo.css">
        <meta charset="UTF-8"></head>
        <body><h1>Ej4-Variabilidad Absoluta y relativa Comunidades</h1>"""
    
    cabecera=data[0]
    
    poblacion=data[1:]
    
    paginaPob+= "<p><table>"
    if ej1 or ej4 or ej5:
        
        paginaPob += "<tr>"
        
        paginaPob+="<th></th>"
        paginaPob+="<th colspan='7'>Variablidad Absoluta</th>"
        paginaPob+="<th colspan='7'>Variablidad Relativa</th>"
        if ej5:
            paginaPob+="<th colspan='7'>Variablidad Absoluta</th>"
            paginaPob+="<th colspan='7'>Variablidad Relativa</th>"
            paginaPob+="<th colspan='7'>Variablidad Absoluta</th>"
            paginaPob+="<th colspan='7'>Variablidad Relativa</th>"
        
        paginaPob+="</tr>"
    paginaPob += "<tr>"
    
    for nomColumna in cabecera:
        paginaPob+="<th>%s</th>" % (nomColumna)
    
    paginaPob+="</tr>"
    
    for reg in poblacion:
        paginaPob+="<tr><td>%s</td>" % (reg[0])
        for i,v in enumerate(reg):
            if i != 0:
                if ej2 or ej3:
                    paginaPob+="<td>{}</td>".format(int(float(v)))
                elif i < 8 or (i > 14 and i < 22) or (i > 28 and i < 35):
                    paginaPob+="<td>{}</td>".format(int(float(v)))
                else:
                    paginaPob+="<td>{}</td>".format(round(float(v),2))
        paginaPob+="</tr>"
        
    
    paginaPob+="</table></p>"
    
    if ej3 or ej5:
        paginaPob += "<img src='"+plot+"' alt='Grafico'/>"
        
    paginaPob += "</body></html>"
    
    f.write(paginaPob)
    f.close()
    
# =============================================================================
# Funcion para el ejercicio 2
# Esta funcion crea y devuelve un diccionario que contiene como clave el numero
# que hace referencia a la comunidad y como valor el nombre de la misma
# =============================================================================
def createAutonomas(n):
    name = n+".htm"
    #Abro el fichero htm donde estan los datos
    with open(name, encoding="utf8") as htmarchivo:
        #Obtengo el iterador al fichero
        entrada = BeautifulSoup(htmarchivo, 'html.parser')
        #Obtengo la tabla dentro del htm que es lo que nos interesa
        table = entrada.table

        #Creo el diccionario
        dict1 = defaultdict(str)
        #Por cada elemento tr de la tabla, obtenemos sus td y los almacenamos
        #en el diccionario como se puede ver en el codigo
        for tr in table.findAll('tr'):
            if(len(tr.findAll('td')) > 1):
                el = tr.findAll('td')
                if el[0].string and el[1].string:
                    dict1[el[0].string.strip()] = el[1].string.strip()
        
    return dict1

# =============================================================================
# Funcion para el ejercicio 2
# Crea y devuelve un diccionario con la relacion entre cada una de las provincias
# con su comunidad autonoma, donde la clave es el codigo de la provincia y el
# valor el codigo de la comunidad autonoma
# =============================================================================
def createProvAuto(n):
    name = n+".htm"
    #Abro el fichero htm donde estan los datos
    with open(name, encoding="utf8") as htmarchivo:
        #Obtengo el iterador al fichero
        entrada = BeautifulSoup(htmarchivo, 'html.parser')
        #Obtengo la tabla dentro del htm que es lo que nos interesa
        table = entrada.table

        #Creo el diccionario
        dict1 = defaultdict(str)
        #Por cada elemento tr de la tabla, obtenemos sus td y los almacenamos
        #en el diccionario como se puede ver en el codigo
        for tr in table.findAll('tr'):
            if(len(tr.findAll('td')) > 1):
                el = tr.findAll('td')
                if el[2].string and el[0].string:
                    dict1[el[2].string.strip()] = el[0].string.strip()
        
    return dict1

# =============================================================================
# Funcion para el ejercicio 2
# Devuelve un numpy donde tenemos todos los datos de las comunidades autonomas
# tanto totales como por sexos
# =============================================================================
def valoresAutonomas(datos,dictAuto,dictProvAuto):
    #Hago una copia de los datos para no modificarlos
    d = datos.copy()
    #Guardo las etiquetas de las comunidades para luego añadirlos a la tabla resultante
    nl = [[e[0]+' '+e[1]] for e in dictAuto.items()]
    #Guardo las claves de las comunidades autonomas para usarlas despues en comparaciones
    nlk = [e[0] for e in dictAuto.items()]
    
    #Creo la cabecera
    cabecera=d[0]
    cabecera[0] = "Comunidad"
    #Elimino la cabecera de los datos
    d.pop(0)
    #Guardo los valores Totales Nacionales ya que esos no varian
    total = d[0]
    #Y los elimino de lso datos
    d.pop(0)
    #Guardo las etiquetas de los datos y creo el np.array solo con los datos numericos
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    
    #Creo el array de salida
    res = np.zeros((len(dictAuto),d.shape[1]))
    #Recorro la matriz de datos por filas
    for i in range(len(d)):
        #Obtengo la key de la comunidad de la fila actual
        k = l[i][0][:2]
        #Busco a que comunidad pertenece esta provincia
        elem = dictProvAuto.get(k)
        #Obtengo la posicion de la comunidad en el array resultante
        pos = nlk.index(elem)
        #Sumo el valor de la fila de la provincia al de la comunidad
        res[pos] += d[i]
    
    #Añado las nuevas etiquetas de las comunidades, el total que ya teniamos
    # y la cabecera
    res = np.hstack((nl,res))
    res = np.vstack((total,res))
    res = np.vstack((cabecera,res))

    return res

# =============================================================================
# Funcion para el ejercicio 3
# Funcion que devuelve un top10 de comunidades con mayor poblacion media
# desde 2010 a 2017
# =============================================================================
def top10(data):
    #Elimino la cabecera y los totales nacionales
    d = data[2:,:]
        
    #Guardo las etiquetas y creo un np array solo con los datos numericos
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    
    #Creo el array resultado
    res = np.zeros((d.shape[0],3))
    #Para cada una de las filas, sumo todos los valores totales y hago la media
    res[:,0] = [sum(e[:8])/8 for e in d]
    #Guardo el valor de los hombre en 2017 (para grafico)
    res[:,1] = d[:,8]
    #Guardo el valor de las mujeres el 2017 (para grafico)
    res[:,2] = d[:,16]        
        
    #Añado las etiquetas y ordeno el array
    res = np.hstack((l,res))
    res = np.array(sorted(res,key=lambda x: float(x[1]), reverse=True))
    
    #Devuelvo las 10 mejores
    return res[:10,:]

# =============================================================================
# Funcion para el ejercicio 3
# Crea un grafico mostrando para las 10 comunidades autonomas con mas poblacion
# media desde 2010 a 2017 el numero de hombres y mujeres en 2017
# =============================================================================
def getplotBar(data): 
    #Obtengo los hombre y las mujeres para ese año
    h = [e[2].astype(float) for e in data]
    m = [e[3].astype(float) for e in data]
    #Guardo las etiquetas
    st = [e[0] for e in data]
    
    #Creo el grafico de barras y lo guardo en un fichero externo
    X = np.arange(10)
    
    plt.figure("barras",figsize=(20, 15))
    plt.bar(X + 0.00, h, color = "r", width = 0.25,label='hombres')
    plt.bar(X + 0.25, m, color = "b", width = 0.25,label='mujeres')
    plt.legend(loc="upper right")
    plt.xticks(X+0.2, st)
    
    plt.savefig('resultados/barrasej3.png')
    
    plt.close()
    
    return "barrasej3.png"

# =============================================================================
# Funcion para el ejercicio 5
# Dibuja un grafico de lineas con la progresion de la poblacion desde 2010
# hasta 2017 para las 10 mejores comunidades autonomas en poblacion media
# =============================================================================
def getplotLines(data):
    
    #Guardo cada uno de los datos para cada una de las comunidades
    lista = [e[2:].astype(float) for e in data]
    #Creo las etiquetas
    st = ["2017","2016","2015","2014","2013","2012","2011","2010"]
    labels = [e[0] for e in data]
    
    #Creo el grafico y lo guardo en un fichero
    X = np.arange(8)

    plt.figure("lineal",figsize=(20, 15))
    for e in lista:
        plt.plot(e)   # Dibuja el gráfico
    plt.title("Poblacion por años")   # Establece el título del gráfico
    plt.xlabel("Año")   # Establece el título del eje x
    plt.ylabel("Poblacion")   # Establece el título del eje y
    plt.legend(labels,loc="upper right")
    plt.xticks(X, st )
    
    plt.savefig('resultados/linesej5.png')
    
    plt.close()
    
    return 'linesej5.png'
    
# =============================================================================
# Funcion para el ejercicio 5
# Crea un top 10 de las comunidades autonomas como la funcion anterior pero
# ahora devuelve todos los datos totales y no únicamente los de hombres y mujeres en 2017
# =============================================================================
def top10Max(data):
    #Me quedo con los datos que me interesan para los calculos
    d = data[2:,:9]
        
    #Guardo las etiquetas y creo el np array solo con los datos numericos
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    
    #Creo el resultado
    res = np.zeros((d.shape[0],d.shape[1]+1))
    #Calculo la media para todas las filas
    res[:,0] = [sum(e[:8])/8 for e in d]
    #Añado el resto de elementos
    res[:,1:] = d[:]        
        
    #Añado las etiquetas y ordeno el array
    res = np.hstack((l,res))
    res = np.array(sorted(res,key=lambda x: float(x[1]), reverse=True))
    
    #Devuelvo los 10 primeros
    return res[:10,:]
    
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
 