import vrep 

def funcinalidad(IDcliente, nombreFicheroElegido, valores): 
    # Inicialización simulador  
    vrep.simxGetObjectHandle(IDcliente, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)
    vrep.simxGetObjectHandle(IDcliente, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
    vrep.simxGetObjectHandle(IDcliente, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)
    vrep.simxGetObjectHandle(IDcliente, 'Vision_sensor', vrep.simx_opmode_oneshot_wait)
    vrep.simxGetStringSignal(IDcliente,'LaserData',vrep.simx_opmode_streaming)

    # Interpretación del nombre del fichero 
    tipo = "enPie"
    if nombreFicheroElegido.find(tipo) == 0: 
        tipoObjeto = "Bill#2"
    tipo = "sentado"
    if nombreFicheroElegido.find(tipo) != 1: 
        tipoObjeto = "Bill"
    tipo = "cilindroMenor"
    if nombreFicheroElegido.find(tipo) != 2: 
        tipoObjeto = "Cylinder1"
    tipo = "cilindroMayor"
    if nombreFicheroElegido.find(tipo) != 3: 
        tipoObjeto = "Cylinder0"
    
    longitud = "Cerca"
    if nombreFicheroElegido.find(tipo) != 0: 
        distanciaMinima = valores["Cerca"]
        distanciaMaxima = valores["Media"]
    longitud = "Media"
    if nombreFicheroElegido.find(tipo) != 1: 
        distanciaMinima = valores["Media"]
        distanciaMaxima = valores["Lejos"]
    longitud = "Lejos"
    if nombreFicheroElegido.find(tipo) != 2: 
        distanciaMinima = valores["Lejos"]
        distanciaMaxima = valores["Lejos"] + 1

          



