# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:21:13 2022

@author: Flor
"""

# Dado el subtotal, calcular el IGV Y EL TOTAL

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtnerIGVconSubtotal(subtotal):.2f}")
print(f"Total: {financieros.obternerTotalconSubtotal(subtotal):.2f}")
