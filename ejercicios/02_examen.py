#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
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
    question = "\033[;36m"+"What is "+a+" x "+b+"? "
    answer = int(input(question))
    a=int(a)
    b=int(b)
    if answer == a*b:
        print ("Well done!")
    else:
        print("No.")
    i = i + 1
print("\033[4;35;47m"+"~~~~Solo 10 intentos~~~~"+'\033[0;m')
