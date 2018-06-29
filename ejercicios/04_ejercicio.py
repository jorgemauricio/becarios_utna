#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#FUNCIONA
"""
#######################################
# Author: Lucrecia Rodríguez
# Email: lucrepbarone@gmail.com
# Date: 2018-06-28
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
dep=0
pago=0
res=0
opcion='a'
while opcion!='S' or opcion!='s':
    opcion=input("Elige la letra de la opción de deseas hacer \n D: Deposito \n P: Pago \n C: Consulta \nS: Salir \n:   ")
    if opcion=='S' or opcion=='s':
        print("Close...")
        opcion=='s'
        break
    elif opcion=='D' or opcion=='d':
        trans=input("Ingresa la cantidad a depositar:  ")
        trans=int(trans)
        dep=dep+trans
        res=dep-pago
        print("deposito: ${} \n".format(trans))
        print("resultado:{}  \n".format(res))
    elif opcion=='P' or opcion=='p':
        trans=input("Ingresa la cantidad a pagar:  ")
        trans=int(trans)
        pago=pago+trans
        res=dep-pago
        print("pago: ${} \n".format(trans))
        print("resultado:{} \n".format(res))
    elif opcion=='c' or opcion=='C':
        print("deposito: ${} \n".format(dep))
        print("pago: ${} \n".format(pago))
        print("resultado:{} \n".format(res))
    else:
        print("Escoge una opción del menú")
        opcion='a'
