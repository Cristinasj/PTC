import math 
x1 = float(input("Primer número: "))
x2 = float(input("Segundo número: "))
x3 = float(input("Tercer número: "))
media = (x1+x2+x3)/3
desviacion = math.sqrt(((x1-media)**2+(x2-media)**2+(x3-media)**2)/3)
print("La desviación típica es {}".format(desviacion))
