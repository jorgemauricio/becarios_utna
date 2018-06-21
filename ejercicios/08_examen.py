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

print("SUMATORIA DE NUMEROS PARES")
acum2=0
for numero in range(0,100):
    if numero % 2==0:
        acum2= acum2+numero
print(acum2)
print("SUMATORIA DE NUMEROS DIVISIBLES ENTRE 5 ")
acum5=0
cont5=0
for numero in range(0,100):
    if(numero % 5==0):
        acum5= acum5+numero
print(acum5)
print("PROMEDIO DE NUMEROS DIVISIBLES ENTRE 7 ")
acum7=0
cont7=0
for numero in range(0,100):
    if(numero % 7==0):
        acum7= acum7+numero
        cont7= cont7+1
print(acum7/cont7)


print("PROMEDIO DE NUMEROS DIVISIBLES ENTRE 5 y 7 ")
acum=0
cont=0

for numero in range(0,100):
    if(numero%5==0) and (numero%7==0):
        acum= acum+numero
        cont= cont+1
print(acum/cont)
