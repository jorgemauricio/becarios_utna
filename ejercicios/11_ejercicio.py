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
Desarrollar un script capaz de generar una simulación de carrera entre dos jugadores
utilizando el modulo random, el primer jugador que llegue a 100 gana la carrera.

Ej.
import random

a = random.randint(1,10)
a: puede ser un valor entre 1 y 10 aleatorio

Para evitar que la simulación se despliegue muy rápido, puedes utilizar el módulo time

import time

time.sleep(1)

el programa detiene su ejecución en 1 segundo

Resultado:

player1: ************************************************************************************************* 97
player2: **************************************************************************************************** 100
player2 wins

"""
import random
import time
from threading import Timer

jugador1=0
jugador2=0
time.sleep(1)

def carrera():
    j1=[]
    j2=[]
    global jugador1
    global jugador2
    jug1= random.randint(1,100)
    jug2= random.randint(1,100)
    jugador1= jug1+jugador1
    jugador2= jug2+jugador2
    for pl1 in range(1,jugador1):
        j1.append("*")
    pla1="".join(j1)
    for pl2 in range(1,jugador2):
        j2.append("*")
    pla2="".join(j2)
    print("Jugador1",pla1)
    print("Jugador2",pla2)
    if jugador1> jugador2:
        print("jugador1 wing")
    else:
        print("jugador2 wing")

print(carrera())
