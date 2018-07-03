#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###########NOFUNCIONAAUN##############
"""
#######################################
# Author: Jaqueline Espinoza
# Email: jaqueespinoza791@gmail.com
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
num1=0
num2=0
num3=0
num4=0
num5=0
for array in matrix:
    for elemento in array:
        if elemento>num1:
            num2=num1
            num3=num1
            num4=num1
            num5=num1
            num1=elemento
        elif elemento>num2:
            num3=num2
            num4=num2
            num5=num2
            num2=elemento
        elif elemento>num3:
            num4=num3
            num5=num3
            num3=elemento
        elif elemento>num4:
            num5=num4
            num4=elemento
        elif elemento>num5:
            num5=elemento

print("1 {}".format(num1))
print("2 {}".format(num2))
print("3 {}".format(num3))
print("4 {}".format(num4))
print("5 {}".format(num5))
y=0

for array in matrix:
    x=0
    for elemento in array:
        if elemento==num1:
            print("valor {}  posicion: {}:{}".format(num1,y,x))
        elif elemento ==num2:
            print("valor {}  posicion: {}:{}".format(num2,y,x))
        elif elemento ==num3:
            print("valor {}  posicion: {}:{}".format(num3,y,x))
        elif elemento ==num4:
            print("valor {}  posicion: {}:{}".format(num4,y,x))
        elif elemento ==num5:
            print("valor {}  posicion: {}:{}".format(num5,y,x))

        x=x+1
    y=y+1
