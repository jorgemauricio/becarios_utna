#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 2
# Valor: 10 puntos
#######################################

De la siguiente matrix de datos, imprime el valor y la posición
de los 5 numéros más altos
matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]

resultado:
Valor 20, posición 0,0
Valor 20, posición 0,2
Valor 20, posición 3,2
Valor 19, posición 1,0
Valor 18, posición 4,2
"""


matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]
print(matrix)
numero1=0
numero2=0
numero3=0
numero4=0
numero5=0

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
