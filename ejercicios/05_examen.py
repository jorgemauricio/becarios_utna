#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#FUNCIONA
"""
#######################################
# Author: Lucrecia Rodríguez
# Email: lucrepbarone@gmail.com
# Date: 2018-06-28
# Version: 1.0
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
numer1=0
numer2=0
numer3=0
numer4=0
numer5=0
for array in matrix:
    for elemento in array:
        if elemento>numer1:
            numer2=numer1
            numer3=numer1
            numer4=numer1
            numer5=numer1
            numer1=elemento
        elif elemento>numer2:
            numer3=numer2
            numer4=numer2
            numer5=numer2
            numer2=elemento
        elif elemento>numer3:
            numer4=numer3
            numer5=numer3
            numer3=elemento
        elif elemento>numer4:
            numer5=numer4
            numer4=elemento
        elif elemento>numer5:
            numer5=elemento

print("1 {}".format(numer1))
print("2 {}".format(numer2))
print("3 {}".format(numer3))
print("4 {}".format(numer4))
print("5 {}".format(numer5))
y=0

for array in matrix:
    x=0
    for elemento in array:
        if elemento==numer1:
            print("valor {}  posicion: {}:{}".format(numer1,y,x))
        elif elemento ==numer2:
            print("valor {}  posicion: {}:{}".format(numer2,y,x))
        elif elemento ==numer3:
            print("valor {}  posicion: {}:{}".format(numer3,y,x))
        elif elemento ==numer4:
            print("valor {}  posicion: {}:{}".format(numer4,y,x))
        elif elemento ==numer5:
            print("valor {}  posicion: {}:{}".format(numer5,y,x))

        x=x+1
    y=y+1

#diccionario[]=lista_numeros



#print("valor {}".format(numer1))
#print("valor {}".format(numer2))
#print("valor {}".format(numer3))
#print("valor {}".format(numer4))
#print("valor {}".format(numer5))
