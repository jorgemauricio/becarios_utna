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

Objetivo: Crear un script el cual de una frase dada, imprima las palabras que su
primer letra sea una s.

frase = "El día de hoy el Sol salió alrededor de las 6 am por segundo día consecutivo"

Resultado:
Sol
salió
segundo
"""

frase = "El día de hoy el Sol salió alrededor de las 6 am por segundo día consecutivo"
for palabra in frase.split():
    if palabra[0].lower()=='s':
        print (palabra)

#funciona
