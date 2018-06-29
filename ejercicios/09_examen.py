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

Dada una palabra mediante una función ordenar sus letras por orden alfabetico

Ej.

palabra = "parangaricutirimicuaro"

Resultado.

aaaaccgiiiimnoprrrrtuu

"""
def main():
    word=[]
    palabra=("parangaricutirimicuaro")
    for letra in palabra:
        word.append(letra)
#print(unaLista)

    ordenar_letras(word)
    word="".join(word)
    print(word)


def ordenar_letras(word): #word
    """
    Función que ordena las letras de una palabra
    param: word: palabra a la cual se le van a ordenar sus letras
    """
    for numPasada in range(len(word)-1,0,-1):
        for i in range(numPasada):
            if word[i]>word[i+1]:
                temp = word[i]
                word[i] = word[i+1]
                word[i+1] = temp







if __name__ == '__main__':
     main()
