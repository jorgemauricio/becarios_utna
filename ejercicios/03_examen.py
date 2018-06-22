#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#*******FUNCIONA******#
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
palabra=input("Ingresa la palabra: ")
pal=palabra.lower()
letra=pal.replace(' ',' ')

if letra== letra[::-1]:
    print("La palabra {} es polindromo".format(palabra))
else:
    print("La palabra {}  no es polindromo".format(palabra))
