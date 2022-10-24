# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:23:16 2022

@author: Flor
"""
archivo =open("archivo_de_prueba.txt","wt")
contenido="Línea1 hola amigos como están?\nLínea2 Bienvenido a la Untels."
archivo.write(contenido)
archivo.close()
