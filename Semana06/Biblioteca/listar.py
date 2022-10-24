# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 12:38:22 2022

@author: Flor
"""

import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")
cursor = conexion.cursor()

consulta = """ SELECT * 
                FROM LIBRO
              
                ORDER BY titulo
            """
cursor = conexion.cursor()
cursor.execute(consulta)
libros = cursor.fetchall()

# Acá libros es una lista... entonces utilizamos un for
for libro in libros:
    print(libro)
conexion.close()
