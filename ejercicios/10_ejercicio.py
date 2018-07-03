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
a="abcdefghjiklmnopqrstuvwxyz"
b="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="1234567890"
s="$#@"
cad="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ1234567890#$@"
contrasena=[]
cont=int(input("Ingrese su longitud de contraseña[8-20]: "))
if cont>=8 and cont<=20:
    contrasena+=random.sample(a,1)
    contrasena+=random.sample(b,1)
    contrasena+=random.sample(n,1)
    contrasena+=random.sample(s,1)
    contrasena+=random.sample(cad,cont-4)
    contrasena="".join(contrasena)
    print(contrasena)
else:
    print("Número fuera de longitud")
