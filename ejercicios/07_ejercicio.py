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
frase="Hola becarios como se encuentran el día de hoy"
frase=frase.split()
pal=[]
def funcion(div,palabra,pal,r):
    div=int(div)
    r=int(r)
    for i in range(1,r):
        pal.append("*")
    for letra in palabra:
        pal.append(letra)
    for i in range(div):
        pal.append("*")
    pal="".join(pal)
    print(pal, "\n\n")

for palabra in frase:
    longitud=float(len(palabra))
    resta=31-longitud
    div=resta/2
    if resta%2==0:
        r=div
        funcion(div,palabra,pal,r)
    else:
        r=div+1
        funcion(div,palabra,pal,r)
    pal=[]
