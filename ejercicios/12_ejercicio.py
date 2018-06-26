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
Dada una matrix de n x n desarrollar un script capaz de identificar el número
mayor que se encuentra en cada una de sus filas, tomando en cuenta que si en la
siguiente fila el número es igual al anterior, este debe de ser actualizdo y
por consiguiente disminuir.


matrix = [[20,1,19,8,6],[2,0,5,8,20],[9,8,23,0,12],[11,2,19,4,5],[4,3,18,1,3]]

Resultado:

Fila 1, número mayor: 8
Fila 2, número mayor: 20
Fila 3, número mayor: 23
Fila 4, número mayor: 19
Fila 5, número mayor: 18

"""
matrix = [[20,1,19,8,6],[2,0,5,8,20],[9,8,23,0,12],[11,2,19,4,5],[4,3,18,1,3]]

num1=0
num2=0
num3=0
num4=0
num5=0
elemento=0

matrix[0]=sorted(matrix[0])
matrix[1]=sorted(matrix[1])
matrix[2]=sorted(matrix[2])
matrix[3]=sorted(matrix[3])
matrix[4]=sorted(matrix[4])

num1= matrix[0][4]
num2= matrix[1][4]
num3= matrix[2][4]
num4= matrix[3][4]
num5= matrix[4][4]

for x in range(5):
    if num1== num2 or num1==num3 or num1==num4 or num1==num5:
        elemento= elemento + 1
        num1= matrix[0][4-elemento]
    elif num2== num1 or num2==num3 or num2==num4 or num2==num5:
        elemento= elemento + 1
        num2= matrix[0][4-elemento]
    elif num3== num1 or num3==num2 or num3==num4 or num3==num5:
        elemento= elemento + 1
        num3= matrix[0][4-elemento]
    elif num4== num1 or num4==num2 or num4==num3 or num4==num5:
        elemento= elemento + 1
        num4= matrix[0][4-elemento]
    elif num5== num1 or num5==num2 or num5==num3 or num5==num4:
        elemento= elemento + 1
        num3= matrix[0][4-elemento]
print(matrix)
print("Fila 1, número mayor: {}".format(num1))
print("Fila 2, número mayor: {}".format(num2))
print("Fila 3, número mayor: {}".format(num3))
print("Fila 4, número mayor: {}".format(num4))
print("Fila 5, número mayor: {}".format(num5))
