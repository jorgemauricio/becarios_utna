#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################

Objetivo:
Un sitio de internet requiere que el password que ingresa el usuario
cumpla con las siguientes caracteristicas para un registro satisfactorio:
1. Al menos un caracter entre [a-z]
2. Al menos un numero entre [0-9]
3. Al menos una letra mayuscula entre [A-Z]
4. Al menos un caracter de los siguientes simbolos [$#@]
5. Longitud mínima de 6 caracteres
6. Longitud máxima de 12 caracteres

Ej.
Si los siguientes passwords los introduce el usuario

passwords = ['HoLa123@7','12345','2w3E*','2We3345']

Resultado:

HoLa123@7
"""
min = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
'x','y','z')
may = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
'Y','Z')
num = ('1','2','3','4','5','6','7','8','9','0')
esp = ('$','#','@')
espa=(' ')
mi = 0
ma = 0
nu = 0
es = 0
espac=0
contrasena= input("Ingresa tu contraseña: ")
if len(contrasena) > 12 and len(contrasena) < 20:
    for caracter in contrasena:
        if caracter in min:
             mi = mi + 1
             #print(mi)
        if caracter in may:
            ma = ma + 1
            #print(ma)
        if caracter in num:
            nu = nu + 1
            #print(nu)
        if caracter in esp:
            es = es + 1
            #print(es)
        if caracter in espa:
            espac = espac + 1
            #print(es)
    if mi < 1:
        print("Falta minuscula")
    if ma < 1:
        print ("Falta mayuscula")
    if nu < 1:
        print("Falta número")
    if es < 1:
        print("Falta simbolo")
    if espac >= 1:
        print("No espacios")
    #if contrasena == '1234' or contrasena == 'ABCD' or contrasena == 'abcd' or contrasena == '#$@':
    #    print("No consecutivamente")
else:
    print("Incorrecto, contraseña debe de contener entre 12 y 20 caracteres")
