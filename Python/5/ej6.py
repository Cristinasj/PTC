#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 11:48:28 2022

@author: cristinasj
"""

# Ejercicio 6 

inventario = {
    'manzanas': {
        'costeCompra': 1.50, 
        'precioVenta': 1.79, 
        'existencias': 3.0
        }, 
    'peras': {
        'costeCompra': 1.50, 
        'precioVenta': 1.80, 
        'existencias': 4.0
        }, 
    'fresas': {
        'costeCompra': 5.0, 
        'precioVenta': 5.20, 
        'existencias': 4.0
        }, 
    'platanos': {
        'costeCompra': 0.9, 
        'precioVenta': 1.1, 
        'existencias': 2.0
        }}



menu = 'MENU \n 1) Vender \n 2) Comprar \n Escribe: '
seleccionFruta = '\n\nSELECCIÓN FRUTA \n manzanas \n peras \n fresas \n platanos \n Escribe: '


accion = 0 
fruta = ''
while(True): 
    print('\nEstado del inventario:')
    print(inventario)
    print()
    accion = input(menu)
    fruta = input(seleccionFruta)
    ganancia = inventario[fruta]['precioVenta'] 
    coste = inventario[fruta]['costeCompra']
    if accion == '1': 
        print('Se ha elegido vender {}'.format(fruta))
        if (float(inventario[fruta]['existencias']) > 0.0): 
            inventario[fruta]['existencias'] -= 1.0
            print('El negocio ha ganado {0:5.2f} euros'.format(ganancia-coste))
        else: 
            print('No ha sido posible efectuar la venta')
    if accion == '2': 
        print('Se ha elegido comprar {}'.format(fruta))
        inventario[fruta]['existencias'] += 1  
        print('La adquisición le ha costado al negocio {0:5.2f} euros'.format(coste))
    print('La cantidad de {} es {}'.format(fruta, inventario[fruta]['existencias']))
    