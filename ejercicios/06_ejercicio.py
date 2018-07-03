#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
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

def fun(dia, mes, año, rango):
    if mes == 12:
        if dia >= 31:
            dia = dia -31 + 1
            mes = 1
            año = año + 1
        else:
            dia = dia + 1
    else:
        mes=mes
        if dia>=rango and mes<12:
            mes=mes+1
            dia=dia-rango +1
        else:
            dia=dia+1

    return dia,mes,año

def fecha(dia, mes, año, hora, minutos):
    año1 = año
    mes1 = mes
    dia1 = dia

    if mes <= 12:
        if mes == 4 or mes == 6 or mes == 9 or mes==11:
            rango = 30
            if dia <= rango:
                dia, mes, año = fun(dia, mes, año, rango)
                print("Fecha: {}-{}-{}  Hora: {}:{}".format(dia, mes, año, hora, minutos))
            else:
                print("Solo 30 días")
        else:
            if mes==2:
                if año % 4 == 0:
                    if dia <= 29:
                        if dia1>28:
                            dia=dia1-29+1
                            mes=mes1+1
                        else:
                            dia=dia1+1
                        if dia==0:
                            dia=29
                            mes=2
                        print("Fecha: {}-{}-{}  Hora: {}:{}".format(dia, mes, año, hora, minutos))

                    else:
                        print("Solo tiene 29 dias")
                else:
                    if dia1<=28 and año%4!=0:
                        if dia1>27:
                            dia=dia1-28+1
                            mes=mes1+1
                        else:
                            dia=dia1+1
                        print("Fecha: {}-{}-{}  Hora: {}:{}".format(dia, mes, año, hora, minutos))
                    else:
                        print("Solo tiene 28 dias")
            else:
                rango=31
                if dia<=rango:
                    dia, mes, año = fun(dia, mes, año, rango)
                    print("Fecha: {}-{}-{}  Hora: {}:{}".format(dia, mes, año, hora, minutos))
                else:
                    print("Solo 31 días")
    else:
        print("Mes no valido")


año = int(input("Ingresar el año: "))
mes = int(input("Ingresar el mes: "))
if mes == 4 or mes == 6 or mes == 9 or mes==11:
    dia = int(input("Ingresa el día[1-30]: "))
    hora = int(input("Ingrear la hora: "))
    minutos = int(input("Ingresar los minutos: "))
elif mes == 2 and año % 4==0:
    dia = int(input("Ingresa el día[1-29]: "))
    hora = int(input("Ingrear la hora: "))
    minutos = int(input("Ingresar los minutos: "))
elif mes == 2:
    dia = int(input("Ingresa el día[1-28]: "))
    hora = int(input("Ingrear la hora: "))
    minutos = int(input("Ingresar los minutos: "))
else:
    dia = int(input("Ingresa el día[1-31]: "))
    hora = int(input("Ingrear la hora: "))
    minutos = int(input("Ingresar los minutos: "))

if minutos < 10:
    minutos = str(minutos)
    minutos = "0" + minutos
    if hora < 10:
        hora = str(hora)
        hora = "0" + hora
    else:
        minutos = str(minutos)
        hora = str(hora)

min = len(str(minutos))
hor = len(str(hora))
print("Minutos: {}  Hora: {}".format(min,hor))

if min == 2 and hor == 2:
    minagregar = int(input("Ingresa los minutos a agregar:  "))
    minutos = int(minutos)
    hora = int(hora)
    suma = minagregar + minutos
    entM = suma//60
    resM = suma % 60
    hora = hora + entM
    minutos = resM

    if hora >= 24:
        enthora = hora // 24
        reshora = hora % 24
        hora = reshora
        suma = minutos + minagregar
        if minutos < 10 or hora < 10:
            if minutos < 10:
                minutos = str(minutos)
                minutos = "0"+minutos
            if hora < 10:
                hora = str(hora)
                hora = "0"+hora
        print("Fecha: {}-{}-{}  Hora: {}:{}".format(dia, mes, año, hora, minutos))
        fecha(dia, mes, año, hora, minutos)

    else:
        enthora = hora // 24
        reshora = hora % 24
        dia=(dia+enthora)
        hora = reshora
        suma = minutos + minagregar
        if minutos < 10 or hora < 10:
            if minutos < 10:
                minutos = str(minutos)
                minutos = "0"+minutos
            if hora < 10:
                hora = str(hora)
                hora = "0"+hora
        print("Fecha: {}-{}-{}  Hora: {}:{}".format(dia, mes, año, hora, minutos))

else:
    print("Minutos ingresados incorrectamente ej: --10:03-- Ó --03:12--")
