#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
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
palabra = input("Ingrese la palabra: ")
pal = palabra.lower()
div =  pal.replace(' ',' ')#Es para dividir

if div == div[::-1]:
    print("La palabra {} es políndromo".format(palabra))
else:
    print("La palabra {} no es políndromo".format(palabra))
