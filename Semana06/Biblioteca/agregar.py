# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:58:11 2022

@author: Flor
"""
import sqlite3
conexion = sqlite3.connect("bdbiblioteca.db")

consulta =""" INSERT INTO
              PAIS(NOMBRE, ESTADO)
              VALUES('BRASIL', 'A')
          """
cursor = conexion.cursor()
cursor.execute(consulta)
conexion.commit()
conexion.close()     