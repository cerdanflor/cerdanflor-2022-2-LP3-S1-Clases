# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:28:13 2022

@author: Flor
"""
# Dado el total, calcular el IGV y el subtotal

import financieros

total = 1000.49
print(f"Subtotal: {financieros.obtenerSubtotalconTotal(total):.2f}")
print(f"IGV: {financieros.obtenerIGVconTotal(total):.2f}")
print(f"Total: {total}")