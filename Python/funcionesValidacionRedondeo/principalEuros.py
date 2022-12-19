import financiacion 
print("Introducir cantidad de dinero: ")
euros = financiacion.leerFloat2Decimales()
print("Introducir interes: ")
interes = financiacion.leerFloat2Decimales()
print("Introducir años: ")
agnos = financiacion.leerInt()
capitalAcumulado = euros 
for i in range(agnos): 
    capitalAcumulado = financiacion.calularCapitalAnual(capitalAcumulado, interes)
print("Capital acumulado: {}".format(financiacion.redondear(capitalAcumulado, 2)))