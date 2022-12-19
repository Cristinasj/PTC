# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import funciones   

def R1 (): 
    directorioDatos = "entradas/"
    directorioResultados = "resultados/"
    fich = directorioDatos+"poblacionProvinciasHM2010-17"
    funciones.limpiarCSV(fich)
    datos = funciones.leerCSV(fich+"Final")
    r1 = funciones.resultado1(datos)
    funciones.crearCSS()
    funciones.array_HTM(r1,directorioResultados+"variacionProvincias",ej1=True)
    return datos
