# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import funciones   

def R4(r2): 
    directorioDatos = "entradas/"
    directorioResultados = "resultados/"
    r4 = funciones.resultado1(r2)
    funciones.array_HTM(r4,directorioResultados+"variacionComAutonomas",ej4=True)
    return r4
