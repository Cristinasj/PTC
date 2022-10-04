# -*- coding: utf-8 -*-    
from math import sqrt 
numero = float(input("Número: "))
raiz = sqrt(numero)

# Primera forma 
print(numero, end=" ")
print(raiz)

# Segunda forma 
print("{0:.4f} {1:.4f}".format(numero, raiz))

# Tercera forma 
print("%.2f" % numero, end=" ")
print("%.2f" % raiz)

# Cuarta forma 
print(f'{numero:.2f}', end=" ")
print(f'raiz:.2f')
