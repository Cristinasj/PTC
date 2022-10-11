def es_numero_o_punto(entrada): 
    return entrada == "0" or entrada == "1" or  entrada == "2" or entrada == "3" or entrada == "4"or entrada == "5" or entrada == "6" or entrada == "7" or entrada == "8" or entrada == "9" or entrada == "."

def validar_euros(entrada): 
    son_euros = True 
    if entrada == "": 
        son_euros = False
    i = 0 
    while son_euros and i < len(entrada):
        if not es_numero_o_punto(entrada[i]): 
            son_euros = False 
        else: 
           i += 1 
    return son_euros

print(validar_euros("333.69")) 