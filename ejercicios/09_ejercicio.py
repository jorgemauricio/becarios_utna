#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
# Version: 1.0
#######################################

Objetivo:
De una matrix dada, encontrar el maximo producto que resulte de la multiplicación
de cinco de sus elementos sin utilizar la función de sorted

matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]

Resultado: 1778400

"""

matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]


numero1 = 0
numero2 = 0
numero3 = 0
numero4 = 0
numero5 = 0

for array in matrix:
    for elemento in array:
        if (elemento > numero1):
            numero2 = numero1
            numero3 = numero1
            numero4 = numero1
            numero5 = numero1
            numero1 = elemento
        elif(elemento > numero2):
            numero3 = numero2
            numero4 = numero2
            numero5 = numero2
            numero2 = elemento
        elif(elemento > numero3):
            numero4 = numero3
            numero5 = numero3
            numero3 = elemento
        elif(elemento > numero4):
            numero5 = numero4
            numero4 = elemento
        elif(elemento > numero5):
            numero5 = elemento
        else:
            print("")

print(numero1, numero2, numero3, numero4, numero5)

mult = numero2 * numero2 * numero3 * numero4 * numero5
print(mult)
