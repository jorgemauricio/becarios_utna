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

De una serie de datos del 0 al 100, realizar
las siguientes acciones:

1. Imprimir la sumatoria de los numeros pares.
2. Imprimir la sumatoria de los numeros divisibles entre 5
3. Imprimir el promedio de los numeros divisibles entre 7
4. Imprimir el promedio de los numeros que sean divisibles entre 2, 5, y 7.
"""
print("SUMATORIA DE LOS NUMEROS PARES")
acum2=0
for num in range(0,100):
    if num%2==0:
        acum2=acum2+num
print(acum2)

acum5=0
print("SUMATORIA DE NUMEROS DIVISIBLES ENTRE CINCO")
for num in range(0,100):
    if num%5==0:
        acum5=acum5+num
print(acum5)
acum7=0
cont7=0
print("PROMEDIO DE NUMEROS DIVISIBLES ENTRE SIETE")
for num in range(0,100):
    if num%7==0:
        acum7=acum7+num
        cont7=cont7+1
print(acum7/cont7)
acum=0
cont=0
print("PROMEDIO DE NUMEROS DIVISIBLES ENTRE CINCO Y SIETE")
for num in range(0,100):
    if num%7==0 and num%5==0:
        acum=acum+num
        cont=cont+1
        #print(num)
print(acum/cont)
