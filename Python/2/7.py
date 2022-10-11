# -*- coding: utf-8 -*-

# Entrada de datos 
nombre = input("Nombre: ")
apellido1 = input("Primer apellido: ")
apellido2 = input("Segundo apellido: ") 

# Calculo de las soluciones parciales
nombreCompleto = nombre + " " + apellido1 + " " + apellido2
nombreReverso = apellido2 + " " + apellido1 + " " + nombre

# Salida de las soluciones 
print("Nombre completo: {}".format(nombreCompleto))
print("Al reves: {}".format(nombreReverso))

# Se escribe el nombre por separado 
print("Separado:")
print(nombre) 
print(apellido1) 
print(apellido2) 
