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
Escribe un programa que calcule el valor neto de una cuenta de banco basado
en las transacciones que se ingresan en la consola de comandos.

Ej:
	D 200
	D 250
	P 300
	D 100
	P 200
	Donde:
	D = Deposito
	P = Pago

Resultado:
	50
"""
contD=0
contp=0
res=0
opcion='a'
while opcion !='S' or opcion !='s':
    opcion, trans= input("Elige la opcion que deseas realizar\n D: Desposito \n P: Pago \n C: Consulta\n S: Salir\n ").split()
    trans=int(trans)
    if opcion=="D" or opcion=="d":
        contD=contD + trans
        res= contD-contp
        print("Deposito: ${}".format(contD))
    elif opcion=="P" or opcion=="p":
        contp=contp + trans
        print("Retiro: ${}".format(contp))
        if contD-contp<0:
            print("Saldo insuficiente")
        else:
            res= contD-contp
    elif opcion=="C" or opcion=="c":
        print("Deposito: ${}\n".format(contD))
        print("Retiro: ${}\n".format(contp))
        print("Saldo actual: ${}\n".format(res))
    elif opcion=="S" or "s":
        print("Close...")
        break
    else:
        print("Ingresar opcion del menú")
        opcion='a'
