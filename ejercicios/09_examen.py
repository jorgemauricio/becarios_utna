#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 9
# Valor: 10 puntos
#######################################

Dada una palabra mediante una función ordenar sus letras por orden alfabetico

Ej.

palabra = "parangaricutirimicuaro"

Resultado.

aaaaccgiiiimnoprrrrtuu

"""

lista=[]
lista_palabra = ("parangaricutirimicuaro")

def ordenamiento(lista):
    for num in range(len(lista)-1,0,-1):
        for j in range(num):
            if lista[j]>lista[j+1]:
                con = lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=con

for letra in lista_palabra:
    lista.append(letra)

ordenamiento(lista)
print(lista)
