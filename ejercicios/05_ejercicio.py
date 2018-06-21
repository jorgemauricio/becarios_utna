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

min=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',
'y','z']
may=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
'Y','Z']
simb=['$','#','@']
num=['1','2','3','4','5','6','7','8','9','0']
espacio=[' ']
contm=0
contM=0
contsim=0
connum=0
conespa=0
contra=input("Ingrese su contraseña con una longitud de 6 a 12 caracteres: ")
if len(contra)>=6 and len(contra)<=12:
    for letra in contra:
        if letra in min:
            contm= contm+1
        if letra in may:
            contM=contM+1
        if letra in simb:
            contsim= contsim+1
        if letra in num:
            connum= connum+1
        if letra in espacio:
            conespa=conespa+1
    if contm>0 and contM>0 and contsim>0 and connum>0 and contespa>0:
        print(contra)
    else:
        if contm==0:
            print(("Te falta una letra en minuscula"))
        if contM==0:
            print("Te falta una letra en mayuscula")
        if contsim==0:
            print("Te faltan simbolos especiales")
        if connum==0:
            print("Te falta un numero")
        if conespa==1:
            print("No debe de llevar espacios")



else:
   print("Contraseña no valida")
