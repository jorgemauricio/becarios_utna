#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jaqueline Espinoza
# Email: jaqueespinoza791@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo: Dada una lista de números, sumar sus dígitos entre sí hasta que el valor,
solo sea un dígito de longitud 1.

listaDeNumeros = [7, 23, 478, 8976, 99999, 901298]

Resultado: 7
Resultado: 5
Resultado: 1
Resultado: 3
Resultado: 9
Resultado: 2

"""

listaDeNumeros=[7, 23, 478, 8976, 99999, 901298]
acum=0
for i in range(len(listaDeNumeros)):
    lista=str(listaDeNumeros[i])
    while len(lista)>1:
        for x in lista:
            #acum=acum+int(x) se puede ambas
            acum+=int(x)
            lista= str(acum)
        acum=0
    print("Resultado:{}".format(lista))
