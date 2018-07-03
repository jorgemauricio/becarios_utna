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

Generar un script capaz de resolver un cuadro mágico, mediante el uso de
machine learning.

El cuadro mágico es una tabla de grado primario donde se dispone de una
serie de números enteros en un cuadrado o matriz de forma tal que la
suma de los números por columnas, filas y diagonales principales sea la misma

Para este ejercicio se va a resolver un cuadrado mágico de 3 x 3, la suma de
sus valores horizontales, verticales y diagonales debe de ser 15.

El valor principal que hay que tomar en cuenta, es el número de iteraciones
que realiza la computadora para resolver este problema.

__|__|__
__|__|__
  |  |

"""

# Librerías
import random
import time
import os
def main():
    cont=0
    Status=True
    while Status:

        numeros=["1","2","3","4","5","6","7","8","9"]
        a1=random.sample(numeros,1)
        a1=" ".join(a1)
        numeros.remove(a1)

        a2=random.sample(numeros,1)
        a2=" ".join(a2)
        numeros.remove(a2)

        a3=random.sample(numeros,1)
        a3=" ".join(a3)
        numeros.remove(a3)

        a4=random.sample(numeros,1)
        a4=" ".join(a4)
        numeros.remove(a4)

        a5=random.sample(numeros,1)
        a5=" ".join(a5)
        numeros.remove(a5)

        a6=random.sample(numeros,1)
        a6=" ".join(a6)
        numeros.remove(a6)

        a7=random.sample(numeros,1)
        a7=" ".join(a7)
        numeros.remove(a7)

        a8=random.sample(numeros,1)
        a8=" ".join(a8)
        numeros.remove(a8)

        a9=random.sample(numeros,1)
        a9=" ".join(a9)

        a1=int(a1)
        a2=int(a2)
        a3=int(a3)
        a4=int(a4)
        a5=int(a5)
        a6=int(a6)
        a7=int(a7)
        a8=int(a8)
        a9=int(a9)
        sum1=a1+a2+a3
        sum2=a4+a5+a6
        sum3=a7+a8+a9

        sum4=a1+a4+a7
        sum5=a2+a5+a8
        sum6=a3+a6+a9

        sum7=a1+a5+a9
        sum8=a3+a5+a7
        cont=cont+1
        #print("###### sumaaa",sum1)
        imprimir_cuadro(a1,a2,a3,a4,a5,a6,a7,a8,a9)
        os.system("clear")
        if sum1==15 and sum2==15 and sum3==15 and sum4==15 and sum5==15 and sum6==15 and sum7==15 and sum8==15:
            #print(sum1)
            #imprimir_cuadro(a1,a2,a3,a4,a5,a6,a7,a8,a9)
            Status=False

    imprimir_cuadro(a1,a2,a3,a4,a5,a6,a7,a8,a9)
    print(cont)
def imprimir_cuadro(a1,a2,a3,a4,a5,a6,a7,a8,a9):
    print("\n")
    print("{}|{}|{}".format(a1,a2,a3))
    print("{}|{}|{}".format(a4,a5,a6))
    print("{}|{}|{}".format(a7,a8,a9))
    print("\n")
    #time.sleep(0.5)

if __name__ == '__main__':
    main()
