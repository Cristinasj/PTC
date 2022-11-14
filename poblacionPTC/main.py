# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import funciones   

if __name__ == "__main__": 
    directorioDatos = "entradasUTF8/"
    directorioResultados = "resultados/"
    ################################################################################
    ############################ Ejercicio 1 ####################################### 
    ################################################################################
    fich = directorioDatos+"poblacionProvinciasHM2010-17"
    funciones.limpiaFichero(fich)
    datos = funciones.readFich(fich+"Final")
    ej1 = funciones.vabsYvrel(datos)
    funciones.createCSS()
    funciones.exportToHTML(ej1,directorioResultados+"variacionProvincias",ej1=True)

    ################################################################################
    ############################ Ejercicio 2 ####################################### 
    ################################################################################
    dictAuto = funciones.createAutonomas(directorioDatos+"comunidadesAutonomas")
    dictProvAuto = funciones.createProvAuto(directorioDatos+"comunidadAutonoma-Provincia")
    ej2 = funciones.valoresAutonomas(datos,dictAuto,dictProvAuto)
    funciones.createCSS()
    funciones.exportToHTML(ej2, directorioResultados+"poblacionComAutonomas",ej2=True)

    ################################################################################
    ############################ Ejercicio 3 ####################################### 
    ################################################################################
    newd = funciones.top10(ej2)
    plot = funciones.getplotBar(newd)
    funciones.createCSS()
    funciones.exportToHTML(ej2,directorioResultados+"poblacionComAutonomas",plot,ej2=True,ej3=True)

    ################################################################################
    ############################ Ejercicio 4 ####################################### 
    ################################################################################
    ej4 = funciones.vabsYvrelSex(ej2)
    funciones.createCSS()
    funciones.exportToHTML(ej4,directorioResultados+"variacionComAutonomas",ej4=True)

    ################################################################################
    ############################ Ejercicio 5 ####################################### 
    ################################################################################
    ej5 = funciones.top10Max(ej2)
    plot = funciones.getplotLines(ej5)
    funciones.createCSS()
    funciones.exportToHTML(ej4,directorioResultados+"variacionComAutonomas",plot,ej4=True, ej5=True)