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
numer1=0
numer2=0
numer3=0
numer4=0
numer5=0
print(matrix[0])
matrix[0]=sorted(matrix[0])
matrix[1]=sorted(matrix[1])
matrix[2]=sorted(matrix[2])
matrix[3]=sorted(matrix[3])
matrix[4]=sorted(matrix[4])
numer1=matrix[0][4]
numer2=matrix[1][4]
numer3=matrix[2][4]
numer4=matrix[3][4]
numer5=matrix[4][4]


cont=0
for i in range(5):
    if numer1==numer2 or numer1==numer3 or numer1==numer4 or numer1==numer5:
        cont=cont+1
        numer1=matrix[0][4-cont]
    if numer2==numer3 or numer2==numer4 or numer2==numer5:
        cont=cont+1
        numer2=matrix[1][4-cont]
    if numer3==numer4 or numer3==numer5:
        cont=cont+1
        numer3=matrix[2][4-cont]
    if numer4==numer5:
        cont=cont+1
        numer4=matrix[3][4-cont]
"""
if numer1==numer2:
    numer1=matrix[0][3]
if numer1==numer4:
    numer1=matrix[0][2]
"""
print(numer1)
print(numer2)
print(numer3)
print(numer4)
print(numer5)
