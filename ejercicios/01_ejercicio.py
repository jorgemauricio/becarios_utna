#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
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

frase = frase.split()

for palabra in frase:
    if (palabra.upper()[0]=='S'):
        print(palabra)
