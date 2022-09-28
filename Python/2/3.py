horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
segundosReal = segundos % 60 
minutosReal = minutos % 60 + segundos//60
horasReal = minutos//60
print("{} horas, {} minutos, {} segundos".format(horasReal, minutosReal, segundosReal))
