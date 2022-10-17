# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:10:23 2022

@author: Flor

Los Módulos te permiten crear librerías de funcionalidades 
que puedas utilizar o reutilizar en cualquier momento en tu proyecto
"""
igv = 0.18
def obtnerIGVconSubtotal(subtotal):
    return subtotal*igv

def obternerTotalconSubtotal(subtotal):
    # subtotal + igv*subtotal
    # subtotal * (1+0.18)
    return subtotal*(1+igv)
# y porque no poner1.18???
# Porque si hago cambios solo necesitaría una línea 10

def obtenerSubtotalconTotal(total):
    return total/(1+igv)

def obtenerIGVconTotal(total):
    return total-obtenerSubtotalconTotal(total)

