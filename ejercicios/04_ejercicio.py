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

contD = 0
contP = 0
res = 0
opcion='a'
while opcion!='S' or opcion!='s':
	opcion, trans=input("Elige la opción que deceas realizar y la cantidad \n D: Deposito \n P: Pago \n C: Consulta \n S: Salir ").split()
	trans=int(trans)
	if opcion=='S' or opcion=='s':
		print("Close...")
		break
	elif opcion=='D' or opcion=='d':
		contD = contD+trans
		res=contD-contP
		print("Deposito: ${}".format(contD))
	elif opcion=='P' or opcion=='p':
		contP = contP+trans
		print("Pago: ${}".format(contP))
		if contD-contP<0:
			print("Saldo insuficiente")
		else:
			res=contD-contP
	elif opcion=='C' or opcion=='c':
		print("Deposito: ${}\n".format(contD))
		print("Retiro: ${}\n".format(contP))
		print("Consulta: ${}\n".format(res))
	else:
		print("Ingrese una opción correcta")
		opcion ='a'
