def es_numero(entrada): 
    return entrada == "1" or entrada == "2" or  entrada == "2" or entrada == "3" or entrada == "4"or entrada == "5" or entrada == "6" or entrada == "7" or entrada == "8" or entrada == "9" 

def validar_euros(entrada): 
    son_euros = True 
    if entrada == "": 
        son_euros = False
    i = 0 
    parte_entera = entrada[0:-3]
    while son_euros and i < len(parte_entera):
        if not es_numero(parte_entera[i]): 
            son_euros = False 
        else: 
           i += 1 
    if not entrada[-3] == ".": 
        son_euros = False 
    if not es_numero(entrada[-1]): 
        son_euros = False 
    if not es_numero(entrada[-2]): 
        son_euros = False
    
    # Conversión a float 
    devolver = 0
    if son_euros: 
        devolver = float(entrada)
    else: 
        while True: 
            a = 0 
    return devolver 

print(validar_euros("333.69")) 