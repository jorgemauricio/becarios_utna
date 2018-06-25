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
player1=0
player2=0
def print_time():
    pla1=[]
    pla2=[]
    p1 = random.randint(1,10)
    p2 = random.randint(1,10)
    global player1
    global player2
    player1=player1+p1
    player2=player2+p2
    for i in range(1,player1):
        pla1.append("*")
    for i in range(1,player2):
        pla2.append("*")
    pla1="".join(pla1)
    pla2="".join(pla2)
    print ("Jugador 1 ",pla1)
    print("jugador 2 ",pla2)
    #return player1,player2
def print_some_times():
    #print (time.time())
    Timer(1, print_time, ()).start()
    #Timer(10, print_time, ()).start()
    time.sleep(1)  # sleep while time-delay events execute
    #print (time.time())
#print_some_times()
x=True
while x==True:
    print_some_times()
    os.system("clear")
    if  player1>=100:
        #print("Jugador 1")
        x=False
    if player2>=100:
        #print("jugador 2")
        x=False
if  player1>=100:
    print(" gano Jugador 1")
if player2>=100:
    print("gano Jugador 2")



#if __name__=='__main__':
    #main()
