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

status = True
cuenta=0
print("BIENVENIDO")
print ("Para hacer un deposito ingresa D y el monto ")
print ("Para hacer un pago ingresa P y el monto ")
print ("Para salir ingresa EXIT ")
transaccion=input("Transaccón \n")
while status:
    if transaccion.upper() == "EXIT":
        print("Cuenta de banco con: {}".format(cuenta))
        break
    elif transaccion.split()[0].upper() == "D":
        cuenta += int(transaccion.split()[1])
        print("Su saldo es de {}".format(cuenta))
    elif transaccion.split()[0].upper() == "P":
        if cuenta - int(transaccion.split()[1]) < 0:
            print("Fondos insuficientes")
        else:
            cuenta -= int(transaccion.split()[1])
            print("su saldo neto es de {}".format(cuenta))
    else:
        print("Error")
    transaccion = input("Transacción:\n")
