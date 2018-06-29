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

Objetivo:
De una matrix dada, encontrar el maximo producto que resulte de la multiplicación
de cinco de sus elementos sin utilizar la función de sorted

matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]

Resultado: 1778400

"""
matrix = [[20,1,20,8,6],[19,0,5,8,10],[9,8,9,0,12],[11,2,13,4,5],[4,3,18,1,3]]
diccionario = dict()
lista_numeros = []
for array in matrix:
    for elemento in array:
        lista_numeros.append(elemento)
nueva_lista=sorted(lista_numeros)
print(nueva_lista[-1] * nueva_lista[-2] * nueva_lista[-3] * nueva_lista[-4] * nueva_lista[-5])
