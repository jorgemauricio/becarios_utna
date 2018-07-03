#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
# Version: 1.0
#######################################

Objetivo:
De una frase, imprimir cada una de sus palabras centradas en un marco de 30
espacios

Ej.
frase = "Hola becarios como se encuentran el día de hoy"

Resultado:
*************hola*************
***********becarios***********
*************como*************
**************se**************
**********encuentran**********
**************el**************
*************dia**************
**************de**************
*************hoy**************
"""

frase = ("Hola bienvenidas al laboratorio nacional de modelaje y sensores remotos del INIFAP gracias por su asistencia")
frase = frase.split()

arr = []
for palabra in frase:
    longitud = len(palabra)
    resta = 31 - longitud
    div = resta / 2
    if resta % 2 == 0:
        div = int(div)
        for i in range(1,div):
            arr.append("*")
        for letra in palabra:
            arr.append(letra)
        for i in range(1,div):
            arr.append("*")
        arr ="".join(arr)
        print(arr)
        arr = []
    else:
        div = int(div)
        for i in range(1,div+1):
            arr.append("*")
        for letra in palabra:
            arr.append(letra)
        for i in range(1,div):
            arr.append("*")
        arr ="".join(arr)
        print(arr)
        arr = []
