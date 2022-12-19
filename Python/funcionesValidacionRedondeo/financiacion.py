def leerFloat2Decimales(): 
    seguirPidiendo=True
    while seguirPidiendo:    
        precio=input("Escribe un número con 2 decimales: ")
        #pruebaExcepcionValueError=float(precio)
        if len(precio)==0:
            print("Introduce un valor")
            esCorrecto=False
        else:         
            esCorrecto=True
        for digito in precio:
            if esCorrecto and (digito!=".") and (digito <'0' or digito >'9'):
                esCorrecto=False
                print("Hay digitos no validos", digito)
        if esCorrecto:
            precioLista=precio.split(".")
            if len(precioLista)==1 or (len(precioLista) >1 and len(precioLista[1])<3):
                #Todo está bien y podemos salir del while de validación
                seguirPidiendo=False
            else: 
                print("Introduce solo con dos decimales")
    return(float(precio))#no se va a producir excepción de valueError 

def leerInt():
    seguirPidiendo=True
    while seguirPidiendo:    
        precio=input("Dime un int: ")
        #pruebaExcepcionValueError=float(precio)
        if len(precio)==0:
            print("Introduce un valor")
            seguirPidiendo=True
        else:         
            seguirPidiendo = False
        for digito in precio:
            if (digito <'0' or digito >'9'):
                seguirPidiendo = True
                print("Hay digitos no validos", digito)
    return(int(precio))#no se va a producir excepción de valueError 

def redondear(numero,decimales):
    numero = numero*10**decimales
    numero += 0.5
    numero = (int)(numero)
    return numero/(10**decimales)

def calularCapitalAnual(capitalInicial,interes):
	return capitalInicial+capitalInicial*interes/100

