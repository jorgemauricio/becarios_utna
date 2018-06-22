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
print(matrix)

for array in matrix:
    for elemento in array:
        if elemento>numero1:
            numero2=numero1
            numero3=numero1
            numero4=numero1
            numero5=numero1
            numero1=elemento
        elif elemento>numero2:
            numero3=numero2
            numero4=numero2
            numero5=numero2
            numero2=elemento
        elif elemento>numero3:
            numero4=numero3
            numero5=numero3
            numero3=elemento
        elif elemento>numero4:
            numero5=numero4
            numero4=elemento
        elif elemento>numero5:
            numero5=elemento
print("1 {}".format(numero1))
print("2 {}".format(numero2))
print("3 {}".format(numero3))
print("4 {}".format(numero4))
print("5 {}".format(numero5))
y=0

for array in matrix:
    x=0
    for elemento in array:
        if elemento==numero1:
            print("Valor {}  Posición: {}:{}".format(numero1,y,x))
        elif elemento ==numero2:
            print("Valor {}  Posición: {}:{}".format(numero2,y,x))
        elif elemento ==numero3:
            print("Valor {}  Posición: {}:{}".format(numero3,y,x))
        elif elemento ==numero4:
            print("Valor {}  Posición: {}:{}".format(numero4,y,x))
        elif elemento ==numero5:
            print("Valor {}  Posición: {}:{}".format(numero5,y,x))

        x=x+1
    y=y+1
