#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
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

def main():
    a1 = False
    a2 = False
    a3 = False
    a4 = False
    a5 = False
    a6 = False
    a7 = False
    a8 = False
    a9 = False

    cont = 0

    arreglo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    status = True

    while status:
        arr = random.sample(arreglo, len(arreglo))
        for x in arr:
            arr[0] = a1
            arr[1] = a2
            arr[2] = a3
            arr[3] = a4
            arr[4] = a5
            arr[5] = a6
            arr[6] = a7
            arr[7] = a8
            arr[8] = a9

            if arr[0] + arr[1] + arr[2] == 15:
                a1 = True
                a2 = True
                a3 = True
            if arr[3] + arr[4] + arr[5] == 15:
                a4 = True
                a5 = True
                a6 = True
            if arr[6] + arr[7] + arr[8] == 15:
                a7 = True
                a8 = True
                a9 = True
            if arr[0] + arr[3] + arr[6] == 15:
                a1 = True
                a4 = True
                a7 = True
            if arr[1] + arr[4] + arr[7] == 15:
                a2 = True
                a5 = True
                a8 = True
            if arr[2] + arr[5] + arr[8] == 15:
                a3 = True
                a6 = True
                a9 = True
            if arr[0] + arr[4] + arr[8] == 15:
                a1 = True
                a5 = True
                a9 = True
            if arr[2] + arr[4] + arr[6] == 15:
                a3 = True
                a5 = True
                a7 = True
            cont =  cont + 1



def imprimir(a1, a2, a3, a4, a5, a6, a7, a8, a9):
    print("\n")
    print("{}|{}|{}".format(a1,a2,a3))
    print("{}|{}|{}".format(a4,a5,a6))
    print("{}|{}|{}".format(a7,a8,a9))
    print("\n")


"""

123 012
456 345
789 678

    cuadro = [a1, a2, a3]
    cuadro1 = [a1]
    cuadro2 = []*num
    for i in range(num):
        cuadro[i] = random.randint(1,3)
        cuadro1[i] = random.randint(1,3)
        cuadro2[i] = random.randint(1,3)

    return cuadro, cuadro1, cuadro2

num = 3
print(main(num))"""
