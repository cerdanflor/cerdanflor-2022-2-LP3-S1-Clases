# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:27:19 2022

@author: Flor
"""

archivo = open("noticia.txt","at")
# \n es para agregar el contenido en una línea al final
contenido="\nFuente: RPP"

archivo.write(contenido)

archivo.close()
