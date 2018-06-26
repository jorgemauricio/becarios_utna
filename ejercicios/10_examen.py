#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 10
# Valor: 10 puntos
#######################################

Generar un script capaz de resolver un cuadro mágico, mediante el uso de
machine learning.

El cuadro mágico es una tabla de grado primario donde se dispone de una
serie de números enteros en un cuadrado o matriz de forma tal que la
suma de los números por columnas, filas y diagonales principales sea la misma

Para este ejercicio se va a resolver un cuadrado mágico de 3 x 3, la suma de
sus valores horizontales, verticales y diagonales debe de ser 15.

El valor principal que hay que tomar en cuenta, es el número de iteraciones
que realiza la computadora para resolver este problema.

__|__|__
__|__|__
  |  |

"""

# Librerías
import random
import time

def main(num):
a1 = [0]
a2 = [0]
a3 = [0]
a4 = [0]
a5 = [0]
a6 = [0]
a7 = [0]
a8 = [0]
a9 = [0]
    cuadro = [a1, a2, a3]
    cuadro1 = []
    cuadro2 = []*num
    for i in range(num):
        cuadro[i] = random.randint(1,3)
        cuadro1[i] = random.randint(1,3)
        cuadro2[i] = random.randint(1,3)

    return cuadro, cuadro1, cuadro2

num = 3
print(main(num))
