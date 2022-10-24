# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 08:40:48 2022

@author: Flor
"""
# Es un ejercicio clásico, tenemos una cadena llamada nombre 
# y se desea que se muestre en formato título

# Importamos la librería
import camelcase

nombre="flor elizabeth cerdán león"
print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con Camelcase.....")

# Imprimimos el nombre en formato titulo, utilizamos camelcas
print(cam.hump(nombre))

# Qué pasaría si ahora el problema pidiera que el 
# nombre de flor y león no se muestre en formato título

# Para resolver el problema
# creamos otro objeto llamado cam2
# al definir el objeto, incluimos los argumentos
# 'flor' y 'león' 

cam2 = camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))


