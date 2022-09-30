x = float(input("X: "))
y = float(input("Y: "))
z = float(input("Z: "))

mayor = x
if (y > x): 
    mayor = y
    if (z > y): 
        mayor = z
menor = x
if (y < x): 
    menor = y
    if (z < y):
        menor = z

print("El mayor es {} y el menor es {}".format(mayor, menor))
