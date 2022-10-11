def contar_letras(palabra, letra): 
    veces = 0
    for a in palabra: 
        if letra == a: 
            veces += 1
    return veces 

p = input("Palabra: ")
l = input("Letra: ")

print(contar_letras(p, l))