def eliminar_letras(palabra, letra): 
    resultado = ""
    for i in range(len(palabra)): 
        if palabra[i] != letra: 
            resultado = resultado + str(palabra[i])
    return resultado 
        
p = input("Palabra: ")
l = input("Letra: ")
print(eliminar_letras(p, l))
