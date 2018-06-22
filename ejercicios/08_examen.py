#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 8
# Valor: 10 puntos
#######################################

De una serie de datos del 0 al 100, realizar
las siguientes acciones:

1. Imprimir la sumatoria de los numeros pares.
2. Imprimir la sumatoria de los numeros divisibles entre 5
3. Imprimir el promedio de los numeros divisibles entre 7
4. Imprimir el promedio de los numeros que sean divisibles entre 2, 5, y 7.
"""


print("Sumatoria de los número pares")
acum2=0
for num in range(0,100):
    if num % 2==0:
        acum2 =  acum2 + num
print(acum2)

print("Sumatoria de los número divisibles entre 5")
acum5=0
for num in range(0,100):
    if num % 5==0:
        acum5 =  acum5 + num
print(acum5)

print("Promedio de los número divisibles entre 7")
acum7=0
cont=0
for num in range(0,100):
    if num % 7==0:
        acum7 =  acum7 + num
        cont =  cont + 1
print(acum7/cont)

print("Promedio de los números divisibles entre 2, 5 y 7")
prom=0
con=0
for num in range(0,100):
    if (num % 2==0) and  (num % 5==0) and (num % 7==0):
        prom =  prom + num
        con = con + 1
print(prom/con)
