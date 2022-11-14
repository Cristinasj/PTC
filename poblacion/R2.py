# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import funciones   

def R2(datos): 
    directorioDatos = "entradas/"
    directorioResultados = "resultados/"
    dictAuto = funciones.crearDiccionarioCA(directorioDatos+"comunidadesAutonomas")
    dictProvAuto = funciones.crearDiccionarioProvincia_CA(directorioDatos+"comunidadAutonoma-Provincia")
    r2 = funciones.resultado2(datos,dictAuto,dictProvAuto)
    funciones.array_HTM(r2, directorioResultados+"poblacionComAutonomas",ej2=True)
    return r2
