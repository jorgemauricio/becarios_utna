#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#FUNCIONA
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 2
# Valor: 10 puntos
#######################################

Script que permita determinar si una palabra es
palíndromo o no.

Palíndromo: es una palabra, número o frase que se lee igual adelante que atrás

ej:

palabra = sOmetEmoS

Resultado:
La palabra sOmetEmoS es palíndromo
"""
#palabra = 'sOmetEmoS'
palabra=input("Ingresa una palabra:  ")
longitud=len(palabra)
#print(longitud)
arr=[]
for letra in palabra:
    arr.append(palabra[longitud-1])
    longitud=longitud-1
    #print(longitud)
arr="".join(arr)
#print(arr)
if palabra.upper()==arr.upper():
    print("la palabra {} es palíndromo".format(palabra))
    print("{}  **  {}".format(palabra,arr))
else:
    print("la palabra {} NO es palíndromo".format(palabra))
