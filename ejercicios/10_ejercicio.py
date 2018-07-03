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
Desarrollar un script que permita geneara un password aleatorio con las siquientes
características mínimas. El usuario puede escoger que su password sea de entre
8 y 20 caracteres.

1. Al menos un caracter entre [a-z]
2. Al menos un numero entre [0-9]
3. Al menos una letra mayuscula entre [A-Z]
4. Al menos un caracter de los siguientes simbolos [$#@]

Resultado:

Introduce la longitud deseada de tu password: 9

H0La123@7
"""


import random

cad = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
'x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','$','#','@')
min = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
'x','y','z')
may = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
'Y','Z')
num = ('1','2','3','4','5','6','7','8','9','0')
esp = ('$','#','@')
x = []
con = int(input("Ingresa el rango de tu contraseña [8-20]: "))
if con >8 and con < 20:
    x += random.sample(cad, con -4)#Es la cadena de caracteres y la longitud
    x += random.sample(min, 1)
    x += random.sample(may, 1)
    x += random.sample(num, 1)
    x += random.sample(esp, 1)
    x = "".join(x)
    print(x)
else:
    print("Numero fuera de longitud")
