#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#FUNCIONA
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
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
a="abcdefghijklmnopqrstuvwxyz"
b="QWERTYUIOPÑLKJHGFDSAZXCVBNM"
n="1234567890"
c="#$&@"
cadena="abcdefghijklmnopqrstuvwxyzQWERTYUIOPÑLKJHGFDSAZXCVBNM1234567890#$&@"
contrasena= []
pwd=int(input("ingresa la longitud de tu contraseña [8-20]:  "))
if pwd>=8 and pwd<=20:
    contrasena+=random.sample(a,1)
    contrasena+=random.sample(b,1)
    contrasena+=random.sample(n,1)
    contrasena+=random.sample(c,1)
    contrasena+=random.sample(cadena,pwd-4)
    contrasena="".join(contrasena)
    print(contrasena)
else:
    print("NO esta en el rango de 8 a 20 caracteres")
