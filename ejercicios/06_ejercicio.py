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
def fecha(d,m,a,hora,minutos):
#a=int(input("ingresa el año: "))
#m=int(input("ingresa el mes: "))
#d=int(input("ingresa el dia: "))
    d1=d
    m1=m
    a1=a
    if m<=12:
        if m==4 or m==6 or m==9 or m==11:
            rango=30
            if d<=rango:
                d,m,a=funcion(d,m,a,rango)
                print("\x1b[1;33m"+"{}-{}-{}    {}:{}".format(d,m,a,hora,minutos))
            else:
                print("este mes solo tiene 30 dias")
        else:
            if m==2:
                if a%4==0:
                    if d<=29:
                        if d1>28:
                            d=d1-29+1
                            m=m1+1
                        else:
                            d=d1+1
                        if d==0:
                            d=29
                            m=2
                        print("\x1b[1;33m"+"{}-{}-{}    {}:{}".format(d,m,a,hora,minutos))

                    else:
                        print("este mes solo tiene 29 dias cada 4 años")
                else:
                    if d1<=28 and a%4!=0:
                        if d1>27:
                            d=d1-28+1
                            m=m1+1
                        else:
                            d=d1+1
                        print("\x1b[1;33m"+"{}-{}-{}    {}:{}".format(d,m,a,hora,minutos))
                    else:
                        print("este mes solo tiene 28 dias")
            else:
                rango=31
                if d<=rango:
                    d,m,a=funcion(d,m,a,rango)
                    print("\x1b[1;33m"+"{}-{}-{}    {}:{}".format(d,m,a,hora,minutos))
                else:
                    print("este mes solo tiene 31 dias")
    else:
        print("mes no valido")


a=int(input("Ingresa el año:  "))
m=int(input("Ingresa el mes:  "))
d=int(input("Ingresa el dia:  "))
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

l1=len(str(minutos))
l2=len(str(hora))
print("min{}  hora  {}".format(l1,l2))
if l1==2 and l2==2:
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
        #d=(d+enteroH)
        hora=residuoH
        sm=min+minutos
        if minutos<10 or hora<10:
            if minutos<10:
                minutos=str(minutos)
                minutos="0"+minutos
            if hora<10:
                hora=str(hora)
                hora="0"+hora
        print("\x1b[1;33m"+"{}-{}-{}    {}:{}".format(d,m,a,hora,minutos))
        fecha(d,m,a,hora,minutos)
    else:
        enteroH=hora//24
        residuoH=hora%24
        d=(d+enteroH)
        hora=residuoH
        sm=min+minutos
        if minutos<10 or hora<10:
            if minutos<10:
                minutos=str(minutos)
                minutos="0"+minutos
            if hora<10:
                hora=str(hora)
                hora="0"+hora

        print("\x1b[1;33m"+"{}-{}-{}    {}:{}".format(d,m,a,hora,minutos))
else:
    print("minutos ingresados incorrectamente ej: --10:03-- Ó --03:12--")
