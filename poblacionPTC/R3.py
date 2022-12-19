# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import funciones   

def R3(r2): 
    directorioDatos = "entradas/"
    directorioResultados = "resultados/"
    newd = funciones.topPoblacion(r2)
    plot = funciones.generarGraficoBarras(newd)
    funciones.array_HTM(r2,directorioResultados+"poblacionComAutonomas",plot,ej2=True,ej3=True)


