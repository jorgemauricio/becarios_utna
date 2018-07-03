#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jaqueline Espinoza
# Email: jaqueespinoza791@gmail.com
# Date: 2018-02-01
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
frase = "Hola becarios como se encuentran el día de hoy"
frase= frase.split()
arr=[]
#print(frase)
for palabra in frase:
    long=len(palabra)
    rest=31-long
    div=rest/2
    if rest%2==0:
        div=int(div)
        for i in range(1,div):
            arr.append("*")
        for letra in palabra:
            arr.append(letra)
        for i in range(1,div):
            arr.append("*")

        arr="".join(arr)
        print(arr)
        arr=[]
    else:
        div=int(div)
        for i in range(1,div+1):
            arr.append("*")
        for letra in palabra:
            arr.append(letra)
        for i in range(1,div):
                arr.append("*")
        arr="".join(arr)
        print(arr)
        arr=[]
