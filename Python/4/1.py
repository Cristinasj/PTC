"""
param: 
    N: lista de enteros
return: 
    suma de todos los valores de N 
"""
def sumatoria (N): 
    suma = 0
    for i in N:
        suma += i
    return suma  
N = input("Lista: ")
N = N.split(" ")
lista = []
for i in N: 
    lista.append(int(i))
print("La sumatoria es {}".format(sumatoria(lista)))
