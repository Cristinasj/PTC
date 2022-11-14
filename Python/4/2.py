def impares(N): 
    devolver = []
    for i in range(len(N)): 
        if i % 2 == 0: 
            devolver.append(N[i])
    return devolver 

N = input("Lista: ")
N = N.split(" ")
lista = []
for i in N: 
    lista.append(int(i))

valores = impares(lista)
print("Los números son: ")
for i in range(len(N/2)): 
    print("Indice {}: valor {} ".format(i*2, valores))