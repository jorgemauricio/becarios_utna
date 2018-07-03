#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
# Version: 1.0
# No. Examen 2
# Valor: 10 puntos
#######################################

Desplegar el 7mo. día a partir de la fecha dada
por el usuario de la siguiente manera

Ingresa el año: 2016
Ingresa el mes [1-12]: 08
Ingresa el día [1-31]: 23
El 7mo día a partir de la fecha es [aaaa-mm-dd] 2016-8-30
"""


año = int(input("Ingresa el año: "))
mes = int(input("Ingresa el mes[1-12]: "))
if mes == 4 or mes == 6 or mes == 9 or mes==11:
    dia = int(input("Ingresa el día[1-30]: "))
elif mes == 2 and año % 4==0:
    dia = int(input("Ingresa el día[1-29]: "))
elif mes == 2:
    dia = int(input("Ingresa el día[1-28]: "))
else:
    dia = int(input("Ingresa el día[1-31]: "))
dia1=dia
mes1=mes
año1=año
if mes <= 12:
    if mes == 4 or mes == 6 or mes == 9 or mes==11:
        if mes >= 12:
            año = año + 1
            mes = 1
        else:
            mes = mes
        if dia > 30:
            print("Solo 30 días")
        else:
            if dia >=25:
                mes = mes + 1
                dia = dia - 30 + 7
            else:
                dia = dia + 7
    else:
        if dia > 31:
            print("Solo 31 días")
        else:
            if dia >=25:
                mes = mes + 1
                dia = dia - 31 + 7
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
                            dia = dia1 - 29 + 7
                            mes = mes1 + 1
                    if dia1 > 28:
                        print("Solo 28 dias")
                    else:
                        dia = dia1 - 28 + 7
                        mes = mes1 + 1

            else:
                dia = dia + 7


    print ("Fecha: {}, {}, {}".format(año, mes, dia))
else:
    print("Mes no valido")
