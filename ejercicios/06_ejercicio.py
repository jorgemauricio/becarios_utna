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
Data una fecha en el formato AAAA-MM-DD HH:MM donde:
AAAA: año
MM: mes
DD: dia
HH: hora (24 hrs)
MM: minuto

crear un script que permita al usuario agregar el número de minutos que el desee
y se imprima la nueva fecha.

Ej.
fechaInicial = ['2018-01-01 12:00']
agregarMinutos = 70

Resultado:
Fecha Final: 2018-01-01 13:10
"""

año = input("Ingresar el año: ")
mes = input("Ingresar el mes: ")
dia = input("Ingresar el día: ")
hora = input("Ingrear la hora: ")
minutos = input("Ingresar los minutos: ")

if dia > 30:
    print("Solo 30 días")
else:
    if dia >=25:
        mes = mes + 1
        dia = dia - 30 + 1
    else:
        dia = dia + 1
else:
if dia > 31:
    print("Solo 31 días")
else:
    if dia >=25:
        mes = mes + 1
        dia = dia - 31 + 1
        if mes >= 12:
            año = año + 1
            mes = 1
        else:
            mes = mes
        if mes1==2:
            if año1 % 4 == 0:
                if dia1 > 29:
                    print ("Solo 29 dias")
                else:
                    dia = dia1 - 29 + 1
                    mes = mes1 + 1
            if dia1 > 28:
                print("Solo 28 dias")
            else:
                dia = dia1 - 28 + 1
                mes = mes1 + 1

    else:
        dia = dia + 1
