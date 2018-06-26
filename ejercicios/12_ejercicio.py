#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo:
Dada una matrix de n x n desarrollar un script capaz de identificar el número
mayor que se encuentra en cada una de sus filas, tomando en cuenta que si en la
siguiente fila el número es igual al anterior, este debe de ser actualizdo y
por consiguiente disminuir.


matrix = [[20,1,19,8,6],[2,0,5,8,20],[9,8,23,0,12],[11,2,19,4,5],[4,3,18,1,3]]

Resultado:

Fila 1, número mayor: 8
Fila 2, número mayor: 20
Fila 3, número mayor: 23
Fila 4, número mayor: 19
Fila 5, número mayor: 18

"""

matrix = [[20,1,19,8,6],[2,0,5,8,20],[9,8,23,0,12],[11,2,19,4,5],[4,3,18,1,3]]

numero1=0
numero2=0
numero3=0
numero4=0
numero5=0
matrix[0] = sorted(matrix[0])
matrix[1] = sorted(matrix[1])
matrix[2] = sorted(matrix[2])
matrix[3] = sorted(matrix[3])
matrix[4] = sorted(matrix[4])

numero1 = matrix[0][4]
numero2 = matrix[1][4]
numero3 = matrix[2][4]
numero4 = matrix[3][4]
numero5 = matrix[4][4]
elemento = 0

for x in range(5):
    if numero1 == numero2 or numero1 == numero3 or numero1 == numero4 or numero1 == numero5:
        elemento = elemento + 1
        numero1 = matrix[0][4-elemento]
    elif numero2 == numero3 or numero2 == numero4 or numero2 == numero5:
        elemento = elemento + 1
        numero2 = matrix[1][4-elemento]
    elif numero3 == numero4 or numero3 == numero5:
        elemento = elemento + 1
        numero3 = matrix[2][4-elemento]
    elif numero4 == numero5:
        elemento = elemento + 1
        numero4 = matrix[3][4-elemento]
print(matrix)
print("Fila 1, numero mayor: {}".format(numero1))
print("Fila 2, numero mayor: {}".format(numero2))
print("Fila 3, numero mayor: {}".format(numero3))
print("Fila 4, numero mayor: {}".format(numero4))
print("Fila 5, numero mayor: {}".format(numero5))
