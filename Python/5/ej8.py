#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 12:19:10 2022

@author: cristinasj
"""

# Ej 8 

equipos = {
    'Marruecos': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        }, 
    'Francia': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'Argentina': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'España': {
        'ganados': 100, 
        'empatados': 0, 
        'perdidos': 0, 
        'puntuacion': 300
        },  
    'Alemania': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'Ignlaterra': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'Italia': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'Holanda': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'Noruega': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        },  
    'EEUU': {
        'ganados': 1, 
        'empatados': 2, 
        'perdidos': 3, 
        'puntuacion': 4
        } 
    }

menu = " 1) Primero  pierde \n 2) Primero gana \n 3) Empate \n Escribe: "
e = list(equipos.keys())
for i in range(0, len(e), 2): 
    print('\n\n{} vs {}'.format(e[i], e[i+1]))
    resultado = input(menu)
    if resultado == '1':   
        print('Gana ' + e[i+1])     
        equipos[e[i]]['perdidos'] += 1
        equipos[e[i+1]]['ganados'] += 1
        equipos[e[i+1]]['puntuacion'] += 3 
    if resultado == '2':
        print('\nGana ' + e[i])
        equipos[e[i+1]]['perdidos'] += 1
        equipos[e[i]]['ganados'] += 1
        equipos[e[i]]['puntuacion'] += 3
    if resultado == '3': 
        print('Empatan ')
        equipos[e[i+1]]['empatados'] += 1
        equipos[e[i]]['empatados'] += 1
        equipos[e[i]]['puntuacion'] += 1
        equipos[e[i+1]]['puntuacion'] += 1


input("Escriba cualquier cosa para ver el resultado ")
print(equipos)