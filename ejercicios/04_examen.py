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

Desplegar el 7mo. día a partir de la fecha dada
por el usuario de la siguiente manera

Ingresa el año: 2016
Ingresa el mes [1-12]: 08
Ingresa el día [1-31]: 23
El 7mo día a partir de la fecha es [aaaa-mm-dd] 2016-8-30
"""
def funcion(dia,mes,año,r):
        if mes>=12:
            año=año+1
            mes=1
            dia=dia-31
        else:
            mes=mes
        if dia>=25 and mes<12:
            mes=mes+1
            dia=dia-r +7
        else:
            dia=dia+7
        return dia,mes,año

a=int(input("ingresa el año: "))
m=int(input("ingresa el mes: "))
d=int(input("ingresa el dia: "))
d1=d
m1=m
a1=a
if m<=12:
    if m==4 or m==6 or m==9 or m==11:
        rango=30
        if d<=rango:
            d,m,a=funcion(d,m,a,rango)
            print("el 7mo día a partir de la fecha es [aaaa-mm-dd]  {} - {} - {}".format(a,m,d))
        else:
            print("este mes solo tiene 30 dias")
    else:
        if m==2:
            if a%4==0:
                if d<=29:
                    if d1>=21:
                        d=d1-29+7
                        m=m1+1
                    else:
                        d=d1+7
                    print("el 7mo día a partir de la fecha es [aaaa-mm-dd]  {} - {} - {}".format(a,m,d))
                else:
                    print("este mes solo tiene 29 dias cada 4 años")
            else:
                if d1<=28 and a%4!=0:
                    if d1>=21:
                        d=d1-28+7
                        m=m1+1
                    else:
                        d=d1+7
                    print("el 7mo día a partir de la fecha es [aaaa-mm-dd]  {} - {} - {}".format(a,m,d))
                else:
                    print("este mes solo tiene 28 dias")
        else:
            rango=31
            if d<=rango:
                d,m,a=funcion(d,m,a,rango)
                print("el 7mo día a partir de la fecha es [aaaa-mm-dd]  {} - {} - {}".format(a,m,d))
            else:
                print("este mes solo tiene 31 dias")
else:
    print("mes no valido")
