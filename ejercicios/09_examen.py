#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jaqueline Espinoza
# Email: jaqueespinoza791@gmail.com
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
def main():
     palabra = "parangaricutirimicuaro"
     lista=[]
     lista_pal=("parangaricutirimicuaro")
     for letra in lista_pal:
         lista.append(letra)

     ordenarmientoPorBuburbuja(lista)
     print(lista)

def ordenarmientoPorBuburbuja(lista):
    for numP in range(len(lista)-1,0,-1):
        for i in range(numP):
            if lista[i]>lista[i+1]:
                con=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=con




if __name__ == '__main__':
     main()
