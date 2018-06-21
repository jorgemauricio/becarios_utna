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
def consecutivo(numero):
    num1=1
    h=0
    for num in numero:
        num=int(num)
        if num1==num-1:
            h=h+1
            num1=num
        else:
            num1=num
    if h>2:
        return True
    else:
        return False

pwd=input("ingresa tu contraseña:  ")
m=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','ñ','z','x','c','v','b','n','m']
M=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ñ','Z','X','C','V','B','N','M']
c=['#','$','@']
n=['1','2','3','4','5','6','7','8','9','0']
e=[" "]
cont1=0
cont2=0
cont3=0
cont4=0
cont5=0
numeros=[]
long=len(pwd)

if long>5 and long<13:
    for letra in pwd:
        if letra in m:
            cont1=cont1+1
        if letra in M:
            cont2=cont2+1
        if letra in c:
            cont3=cont3+1
        if letra in n:
            cont4=cont4+1
            numeros.append(letra)
        if letra in e:
            cont5=cont5+1

    if cont1!=0 and cont2!=0 and cont3!=0 and cont4!=0:
        if consecutivo(numeros)==True:
            print("Numeros consecutivos")
        else:
            print("Contraseña correcta  :{}".format(pwd))
            if cont5>0:
                print("tu contraseña tiene {} espacios :)".format(cont5))
    else:
        if cont1==0:
            print("No tiene minusculas")
        if cont2==0:
            print("No tiene mayusculas")
        if cont3==0:
            print("No tiene algun caracter")
        if cont4==0:
            print("No tiene números")
else:
    print("El rango de la contraseña debe ser mayor a 6 y menor a 12")
