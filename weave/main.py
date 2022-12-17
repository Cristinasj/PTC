import weave 
import time 
import numpy as np 
import matplotlib.pyplot as plt

def holaMundo(entrada): 
    code = """
        return_val = entrada*2;  
    """
    return weave.inline(code, ['entrada'], compiler='gcc')

# SUMATORIA

def sumatoriaPython(entrada):
    suma = 0  
    for i in range(entrada): 
        suma += i 
    return suma

def sumatoriaWeave(entrada):
    code =  """
            int suma = 0;  
            for (int i = 0; i < entrada; i++)
            {
               suma += i;
            }
            return_val = suma;  
            """
    return weave.inline(code,['entrada'],compiler='gcc')

# SUMA RAICES 

def sumaRaizPython(entrada): 
    suma = 0
    for i in range(entrada): 
        suma += i**(1/2)
    return suma 

def sumaRaizWeave(entrada): 
    code = """
            int suma = 0; 
            for (int i = 0; i < entrada; i++) {
                suma += sqrt(i); 
            }
            return_val = suma;  
    """
    return weave.inline(code,['entrada'],compiler='gcc')

# CRONOMETRAJE DE LAS EJECUCIONES 

MUCHAS_VECES = 1000
OTRAS_MUCHAS_VECES = 10000
resultadosSumatoriaPython = []
resultadosSumatoriaWeave = []
resultadosRaizPython = []
resultadosRaizWeave = []
indices = []

for e in range(1, OTRAS_MUCHAS_VECES, 100): 

    indices.append(e)

    print("{0:5.6f} %".format(float(e)/(OTRAS_MUCHAS_VECES)*100))
    # Comparacion de sumatorias

    t1p_ini = time.time() 
    for i in range(MUCHAS_VECES): 
        sumatoriaPython(e)
    t1p_fin = time.time() 

    tsumatoriaPython = t1p_fin - t1p_ini
    resultadosSumatoriaPython.append(tsumatoriaPython) 

    t1w_ini = time.time() 
    for i in range(MUCHAS_VECES): 
        sumatoriaWeave(e)
    t1w_fin = time.time() 

    tsumatoriaWeave = t1w_fin - t1w_ini 
    resultadosSumatoriaWeave.append(tsumatoriaWeave)

    # Comparacion raiz 

    t2p_ini = time.time() 
    for i in range(MUCHAS_VECES): 
        sumaRaizPython(e)
    t2p_fin = time.time() 

    tRaizPython = t2p_fin - t2p_ini 
    resultadosRaizPython.append(tRaizPython)

    t2w_ini = time.time() 
    for i in range(MUCHAS_VECES): 
        sumaRaizWeave(e)
    t2w_fin = time.time() 

    tRaizWeave = t2w_fin - t2w_ini 
    resultadosRaizWeave.append(tRaizWeave)

# GRAFICAS DE LOS RESULTADOS 
fig,ax=plt.subplots()
ax.set_title("Sumatoria")
ax.plot(indices, resultadosSumatoriaPython)       
ax.plot(indices, resultadosSumatoriaWeave)
ax.set_ylabel("Segundos")
ax.set_xlabel("Tam. de la entrada")
ax.legend(["Python","Weave"])
plt.show()
fig,ax=plt.subplots()
ax.set_title("Suma de raices")
ax.plot(indices, resultadosRaizPython)       
ax.plot(indices, resultadosRaizWeave)
ax.set_ylabel("Segundos")
ax.set_xlabel("Tam. de la entrada")
ax.legend(["Python","Weave"])
plt.show()