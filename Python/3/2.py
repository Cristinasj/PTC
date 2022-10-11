def eliminar_letras(palabra, letra): 
    resultado = ""
    for i in range(len(palabra)): 
        if palabra[i] != letra: 
            resultado[i] = letra
        
p = input("Palabra: ")
l = input("Letra: ")
p = (eliminar_letras(p, l))
