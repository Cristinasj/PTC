# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import funciones   

def R5(r2,r4): 
    directorioDatos = "entradas/"
    directorioResultados = "resultados/"
    r5 = funciones.top10Max(r2)
    plot = funciones.generarGraficoLineas(r5)
    funciones.array_HTM(r4,directorioResultados+"variacionComAutonomas",plot,ej4=True, ej5=True)