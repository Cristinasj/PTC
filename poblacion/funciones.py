# -*- coding: utf-8 -*-
import csv
import numpy as np
from bs4 import BeautifulSoup
from collections import defaultdict
import matplotlib.pyplot as plt

"""
    param: 
        nombre del archivo
    efecto:
        crea un fichero limpio 
"""
def limpiarCSV(n):
    nombre = n+".csv"
    ficheroInicial=open(nombre,"r", encoding="utf8")
    cadenaPob=ficheroInicial.read()
    ficheroInicial.close()
    primero=cadenaPob.find("Total Nacional")
    ultimo=cadenaPob.find("Notas")
    cadenaFinal=cadenaPob[primero:ultimo]
    cabecera="Provincia;T2017;T2016;T2015;T2014;T2013;T2012;T2011;T2010;H2017;H2016;H2015;H2014;H2013;H2012;H2011;H2010;M2017;M2016;M2015;M2014;M2013;M2012;M2011;M2010"
    nombre = n+"Final.csv"
    ficheroFinal=open(nombre, "w",encoding="utf8")
    ficheroFinal.write(cabecera+'\n'+cadenaFinal)
    ficheroFinal.close()
 
"""
    param: 
        nombre del archivo 
    salida: 
        lista de diccionarios con el contenido del csv 
""" 
def leerCSV(n):
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

"""
    param:  
        lista de diccionarios con la información sobre la población de las provincias 
    salida: 
        numpy array con los resultados 
"""
def resultado1(datos):
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

"""
    param: 
        lista de diccionarios con los datos 
    salida: 
        numpy array con el resultado
"""
def resultado2(datos):
    d = datos.copy()
    cabecera=["Comunidad","T2017","T2016","T2015","T2014","T2013","T2012","T2011","T2017","T2016","T2015","T2014","T2013","T2012","T2011"]
    cabecera.extend(["H2017","H2016","H2015","H2014","H2013","H2012","H2011","H2017","H2016","H2015","H2014","H2013","H2012","H2011"])
    cabecera.extend(["M2017","M2016","M2015","M2014","M2013","M2012","M2011","M2017","M2016","M2015","M2014","M2013","M2012","M2011"])
    d = d[1:,:]
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    desp = 7
    res = np.zeros((d.shape[0],desp*6))
    for i in range(desp):
        res[:,i] = d[:,i]-d[:,i+1]
        res[:,i+desp] = (d[:,i]-d[:,i+1])/d[:,i+1]*100
        res[:,i+desp*2] = d[:,i+desp+1]-d[:,i+desp+2]
        res[:,i+desp*3] = (d[:,i+desp+1]-d[:,i+desp+2])/d[:,i+desp+2]*100
        res[:,i+desp*4] = d[:,i+desp*2+2]-d[:,i+desp*2+3]
        res[:,i+desp*5] = (d[:,i+desp*2+2]-d[:,i+desp*2+3])/d[:,i+desp*2+3]*100
    res = np.hstack((l,res))
    res = np.vstack((cabecera,res))
    return res

"""
    efecto: 
        Crea un fichero CSS con un estilo predeterminado 
"""
def crearCSS():
    fileEstilo=open("entradas/estilo.css","w")
    estilo="""  table, th, td {
                    border-collapse: collapse;    
                    border:1px solid black;
                    font-family: Arial, Helvetica, sans-serif;
                    padding: 8px;
                    
                }  """
    fileEstilo.write(estilo)
    fileEstilo.close()

"""
    param: 
        - data: numpy array 
        - fich: nombre del fichero HTML resultante 
        - plot: flag para saber si tiene una imagen
        - ej1-ej5: flags para personalizar el formato del HTM
    efecto: 
        Crea un fichero html con las características necesarias 
"""
def array_HTM(data,fich,plot=None,ej1=False,ej2=False,ej3=False,ej4=False,ej5=False):
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
    
"""
    param: 
        Nombre del fichero csv 
    salida: 
        diccionario id-nombre de CA 
"""
def crearDiccionarioCA(n):
    name = n+".htm"
    with open(name, encoding="utf8") as htmarchivo:
        entrada = BeautifulSoup(htmarchivo, 'html.parser')
        table = entrada.table
        dict1 = defaultdict(str)
        for tr in table.findAll('tr'):
            if(len(tr.findAll('td')) > 1):
                el = tr.findAll('td')
                if el[0].string and el[1].string:
                    dict1[el[0].string.strip()] = el[1].string.strip()
    return dict1

"""
    param: 
        Nombre del fichero csv 
    salida: 
        Diccionario con id de provincia- CA correspondiente 
"""
def crearDiccionarioProvincia_CA(n):
    name = n+".htm"
    with open(name, encoding="utf8") as htmarchivo:
        entrada = BeautifulSoup(htmarchivo, 'html.parser')
        table = entrada.table
        dict1 = defaultdict(str)
        for tr in table.findAll('tr'):
            if(len(tr.findAll('td')) > 1):
                el = tr.findAll('td')
                if el[2].string and el[0].string:
                    dict1[el[2].string.strip()] = el[0].string.strip()
    return dict1

"""
    param: 
        - datos: lista de diccionarios con la información 
        - diccionario id-CA 
        - diccionario id de provincia - id de CA 
    salida: 
        array numpy con los calculos completos (total y por sexos)
"""
def resultado2(datos,dictAuto,dictProvAuto):
    d = datos.copy()
    nl = [[e[0]+' '+e[1]] for e in dictAuto.items()]
    nlk = [e[0] for e in dictAuto.items()]
    cabecera=d[0]
    cabecera[0] = "Comunidad"
    d.pop(0)
    total = d[0]
    d.pop(0)
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    res = np.zeros((len(dictAuto),d.shape[1]))
    for i in range(len(d)):
        k = l[i][0][:2]
        elem = dictProvAuto.get(k)
        pos = nlk.index(elem)
        res[pos] += d[i]
    res = np.hstack((nl,res))
    res = np.vstack((total,res))
    res = np.vstack((cabecera,res))
    return res

"""
    param: 
        - array numpy con los calculos completos (total y por sexos)
    salida: 
        - array numpy solo con las CCAA con más población 
"""
def topPoblacion(data):
    d = data[2:,:]
    l = [[e[0]] for e in d]
    d = np.array(d)[:,1:].astype(float)
    res = np.zeros((d.shape[0],3))
    res[:,0] = [sum(e[:8])/8 for e in d]
    res[:,1] = d[:,8]
    res[:,2] = d[:,16]        
    res = np.hstack((l,res))
    res = np.array(sorted(res,key=lambda x: float(x[1]), reverse=True))
    return res[:10,:]

"""
    param: 
        - array numpy con población total y por sexos de cada CA 
    return: 
        - nombre de la imagen resultante
    efecto: 
        - genera una imagen png   

"""
def generarGraficoBarras(data): 
    h = [e[2].astype(float) for e in data]
    m = [e[3].astype(float) for e in data]
    st = [e[0] for e in data]
    X = np.arange(10)
    plt.figure("barras",figsize=(20, 15))
    plt.bar(X + 0.00, h, color = "r", width = 0.25,label='hombres')
    plt.bar(X + 0.25, m, color = "b", width = 0.25,label='mujeres')
    plt.legend(loc="upper right")
    plt.xticks(X+0.2, st)
    plt.savefig('imagenes/R3.png')
    plt.close()
    return "imagenes/R3.png"




if __name__ == "__main__":
    print("test") 