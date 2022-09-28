precio = float(input("Precio bruto del vehículo: "))
ganancia = float(input("Porcentaje de ganancia del vendedor: ")) 
iva = float(input("Iva a aplicar: "))
base = precio + precio*ganancia 
final = base + base*iva 
print("El precio final es {}".format(final))
