import financiacion 
from decimal import Decimal, getcontext 
print("Introducir cantidad de dinero: ")
euros = financiacion.leerFloat2Decimales()
print("Introducir interes: ")
interes = financiacion.leerFloat2Decimales()
print("Introducir años: ")
agnos = financiacion.leerInt()
eurosD = Decimal(euros)
interesD = Decimal(interes)
capitalAcumulado = eurosD
for i in range(agnos): 
    capitalAcumulado += capitalAcumulado*interesD
print("Capital acumulado: {}".format(capitalAcumulado))