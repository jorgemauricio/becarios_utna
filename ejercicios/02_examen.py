#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jaqueline Espinoza
# Email: jaqueespinoza791@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 2
# Valor: 9 puntos
#######################################

Corrigue el siguiente script, recuerda realizar tus commits cada 5 min.
"""
import random
a = random.randint(1,12)
b = random.randint(1,12)
i=0
while i in range(10):
    a=str(a)
    b=str(b)
    question = "What is "+a+" x "+b+"?"
    answer = int(input(question))
    a=int(a)
    b=int(b)
    if answer == a*b:
        print ("\x1b[1;33m"+"Well done!")
        i=11
    else:
        print("No.")
        i=i+1
    if i==10:
        print("\033[4;35;47m"+"Número de intentos excedidos"+"\033[0;m")
