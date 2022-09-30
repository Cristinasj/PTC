# Una bebida con graduación de x grados tendrá en su composición x cc de alcohol por cada 100 cc 
graduacion = float(input("Graduación: "))
volumen = 333 
alcohol = 50
cantidad_posible = alcohol/graduacion
unidades = cantidad_posible // volumen 
print("Puedes beber {0:n} tercios".format(unidades))
