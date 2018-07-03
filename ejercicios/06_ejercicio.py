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
def funcion(dia,mes,año,r):
        if mes==12:

            if dia>=31:
                dia=dia-31+1
                año=año+1
                mes=1
            else:
                dia=dia+1

        else:
            mes=mes
            if dia>=r and mes<12:
                mes=mes+1
                dia=dia-r +1
            else:
                dia=dia+1
        return dia,mes,año
def fecha(dia,mes,año,hora,minutos):

    d1=dia
    m1=mes
    a1=año
    if mes<=12:
        if mes==4 or mes==6 or mes==9 or mes==11:
            rango=30
            if dia<=rango:
                dia,mes,año=funcion(dia,mes,año,rango)
                print("{}-{}-{}    {}:{}".format(dia,mes,año,hora,minutos))
            else:
                print("este mes solo tiene 30 dias")
        else:
            if mes==2:
                if año%4==0:
                    if dia<=29:
                        if d1>28:
                            dia=d1-29+1
                            mes=m1+1
                        else:
                            dia=d1+1
                        if dia==0:
                            dia=29
                            mes=2
                        print("{}-{}-{}    {}:{}".format(dia,mes,año,hora,minutos))

                    else:
                        print("este mes solo tiene 29 dias cada 4 años")
                else:
                    if d1<=28 and año%4!=0:
                        if d1>27:
                            dia=d1-28+1
                            mes=m1+1
                        else:
                            dia=d1+1
                        print("{}-{}-{}    {}:{}".format(dia,mes,año,hora,minutos))
                    else:
                        print("este mes solo tiene 28 dias")
            else:
                rango=31
                if dia<=rango:
                    dia,mes,año=funcion(dia,mes,año,rango)
                    print("{}-{}-{}    {}:{}".format(dia,mes,año,hora,minutos))
                else:
                    print("este mes solo tiene 31 dias")
    else:
        print("mes no valido")


año=int(input("Ingresa el año:  "))
mes=int(input("Ingresa el mes:  "))
dia=int(input("Ingresa el dia:  "))
hora=int(input("Ingresa la hora:  "))
minutos=int(input("Ingresa los minutos:  "))


if minutos<10:
    minutos=str(minutos)
    minutos="0"+minutos
    if hora<10:
        hora=str(hora)
        hora="0"+hora
else:
    minutos=str(minutos)
    hora=str(hora)

minu=len(str(minutos))
hor=len(str(hora))
#print("minutos{}  hora  {}".format(minu,hor))
if minu==2 and hor==2:
    min=int(input("Ingresa los minutos que deseas agregar:  "))
    minutos=int(minutos)
    hora=int(hora)
    sm=min+minutos
    enteroM=sm//60
    residuoM=sm%60
    hora=hora+enteroM
    minutos=residuoM
    if hora>=24:
        enteroH=hora//24
        residuoH=hora%24
        hora=residuoH
        sm=min+minutos
        if minutos<10 or hora<10:
            if minutos<10:
                minutos=str(minutos)
                minutos="0"+minutos
            if hora<10:
                hora=str(hora)
                hora="0"+hora
        print("{}-{}-{}    {}:{}".format(dia,mes,año,hora,minutos))
        fecha(dia,mes,año,hora,minutos)
    else:
        enteroH=hora//24
        residuoH=hora%24
        dia=(dia+enteroH)
        hora=residuoH
        sm=min+minutos
        if minutos<10 or hora<10:
            if minutos<10:
                minutos=str(minutos)
                minutos="0"+minutos
            if hora<10:
                hora=str(hora)
                hora="0"+hora

        print("{}-{}-{}    {}:{}".format(dia,mes,año,hora,minutos))
else:
    print("minutos ingresados incorrectamente ej: --10:03-- Ó --03:12--")
