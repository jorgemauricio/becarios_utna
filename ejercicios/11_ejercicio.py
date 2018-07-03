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
import os
from threading import Timer

player1 = 0
player2 = 0
time.sleep(1)

def carrera():
    p1 = []
    p2 = []
    global player1
    global player2
    pl1 = random.randint(1,100)
    pl2 = random.randint(1,100)
    player1 = pl1 + player1
    player2 = pl2 + player2
    for j1 in range(1, pl1):
        p1.append("*")
    pla1 ="".join(p1)
    for j2 in range(1, pl2):
        p2.append("*")
    pla2 ="".join(p2)
    print("Player1", pla1)
    print("Player2", pla2)
    if player1 > player2:
        print("Player1 Wing")
    else:
        print("Player2 Wing")

print(carrera())
