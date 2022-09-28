precio = float(input("Precio: "))
pago = float(input("Cantidad entregada por el cliente: "))
devolucion = pago - precio
devolucion = devolucion * 100
dosEuros = devolucion // 200 
euro = (devolucion - dosEuros*200) // 100
cincuenta = (devolucion - dosEuros*200 - euro*100) // 50 
veinte = (devolucion - dosEuros*200 - euro*100 - cincuenta*50) // 20 
diez = (devolucion - dosEuros*200 - euro*100 - cincuenta*50 - veinte*20) // 10
cinco = (devolucion - dosEuros*200 - euro*100 - cincuenta*50 - veinte*20 - diez*10) // 5
dos = (devolucion - dosEuros*200 - euro*100 - cincuenta*50 - veinte*20 - diez*10 - cinco*5) // 2
uno = (devolucion - dosEuros*200 - euro*100 - cincuenta*50 - veinte*20 - diez*10 - cinco*5 - dos*2)
print("{0:n} de 2.00".format(dosEuros))
print("{0:n} de 1.00".format(euro))
print("{0:n} de 0.50".format(cincuenta))
print("{0:n} de 0.20".format(veinte))
print("{0:n} de 0.10".format(diez))
print("{0:n} de 0.05".format(cinco))
print("{0:n} de 0.02".format(dos))
print("{0:n} de 0.01".format(uno))
