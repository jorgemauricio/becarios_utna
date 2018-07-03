#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
# Version: 1.0
# No. Examen 2
# Valor: 9 puntos
#######################################

Solucionar los siguientes puntos mediante un script:
1) Del archivo examen_final.csv genera un archivo csv para cada día, estos csv
deben de guardarse en la carpeta de resultados
2) De la información que se tiene, genera un corte de información para las columnas
Lat y Long con los siguientes valores

Lat > 21.0
Lat < 24.0
Long > -104.0
Long < -100.0

3) Calcula las medias de cada una de las variables Rain, Tmax, Tmin por día
y guardalas en un csv en la carpeta de resultados

4) Calcula las medias de cada una de las variables Rain, Tmax, Tmin por día
del corte de información limitado por las columnas Lat y Long con los siguientes
valores:

Lat > 21.0
Lat < 24.0
Long > -104.0
Long < -100.0

y guardalas en un csv en la carpeta de resultados

5) Calcular las Unidades Calor (UC) para cada una de las filas con la formúla
que se indica en el programa.
"""

# librerias

import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")

df = pd.read_csv("/home/caro/Documentos/becarios_utna/ejercicios/examen_final.csv")


d1 = df.ix[0:24298]#dia 1
d2 = df.ix[24299:92597]#dia 2
d3 = df.ix[92598:138896]#dia 3
d4 = df.ix[138897:185195]#dia 4
d5 = df.ix[185196:231495]#dia 5

a = df[(df['Lat']>21.0) & (df['Lat']<24.0) & (df['Long']> -104.0) & (df['Long']< -100.0)] #Latitud y Longitud

#Funciones para crear archivos
def dia1_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia1.csv','w')
    archivo.close()
def dia2_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia2.csv','w')
    archivo.close()
def dia3_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia3.csv','w')
    archivo.close()
def dia4_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia4.csv','w')
    archivo.close()
def dia5_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia5.csv','w')
    archivo.close()

def latlong_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/LatLong.csv','w')
    archivo.close()

def PromediosLatLong_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/PromediosLatLong.csv','w')
    archivo.close()

def Promedios_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Promedios.csv','w')
    archivo.close()

def UC_crear():
    archivo = open ('/home/caro/Documentos/becarios_utna/ejercicios/Resultados/UC.csv','w')
    archivo.close()

#Funciones para escribir el archivo
def dia1_escribir():
    x = pd.DataFrame.to_csv(d1)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia1.csv","a")
    archivo.write(x)
def dia2_escribir():
    x = pd.DataFrame.to_csv(d2)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia2.csv","a")
    archivo.write(x)
def dia3_escribir():
    x = pd.DataFrame.to_csv(d3)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia3.csv","a")
    archivo.write(x)
def dia4_escribir():
    x = pd.DataFrame.to_csv(d4)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia4.csv","a")
    archivo.write(x)
def dia5_escribir():
    x = pd.DataFrame.to_csv(d5)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Dia5.csv","a")
    archivo.write(x)

def latlong_escribir():
    x = pd.DataFrame.to_csv(a)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/LatLong.csv","a")
    archivo.write(x)

def PromediosLatLong_escribir():
    dr1 = a['Rain'].ix[0:24298].mean()
    dtma1 = a['Tmax'].ix[0:24298].mean()
    dtmi1 = a['Tmin'].ix[0:24298].mean()
    dr2 = a['Rain'].ix[24299:92597].mean()
    dtma2 = a['Tmax'].ix[24299:92597].mean()
    dtmi2 = a['Tmin'].ix[24299:92597].mean()
    dr3 = a['Rain'].ix[92598:138896].mean()
    dtma3 = a['Tmax'].ix[92598:138896].mean()
    dtmi3 = a['Tmin'].ix[92598:138896].mean()
    dr4 = a['Rain'].ix[138897: 185195].mean()
    dtma4 = a['Tmax'].ix[138897: 185195].mean()
    dtmi4 = a['Tmin'].ix[138897: 185195].mean()
    dr5 = a['Rain'].ix[185196:231495].mean()
    dtma5 = a['Tmax'].ix[185196:231495].mean()
    dtmi5 = a['Tmin'].ix[185196:231495].mean()
    dr1 = str(dr1)
    dtma1 = str(dtma1)
    dtmi1 = str(dtmi1)
    dr2 = str(dr2)
    dtma2 = str(dtma2)
    dtmi2 = str(dtmi2)
    dr3 = str(dr3)
    dtma3 = str(dtma3)
    dtmi3 = str(dtmi3)
    dr4 = str(dr4)
    dtma4 = str(dtma4)
    dtmi4 = str(dtmi4)
    dr5 = str(dr5)
    dtma5 = str(dtma5)
    dtmi5 = str(dtmi5)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/PromediosLatLong.csv","a")
    archivo.write("PROMEDIOS DE LOS 5 DIAS LATITUD Y LONGITUD \n ")
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr1, dtma1, dtmi1))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr2, dtma2, dtmi2))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr3, dtma3, dtmi3))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr4, dtma4, dtmi4))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr5, dtma5, dtmi5))

def Promedios_escribir():
    dr1 = df['Rain'].ix[0:24298].mean()
    dtma1 = df['Tmax'].ix[0:24298].mean()
    dtmi1 = df['Tmin'].ix[0:24298].mean()
    dr2 = df['Rain'].ix[24299:92597].mean()
    dtma2 = df['Tmax'].ix[24299:92597].mean()
    dtmi2 = df['Tmin'].ix[24299:92597].mean()
    dr3 = df['Rain'].ix[92598:138896].mean()
    dtma3 = df['Tmax'].ix[92598:138896].mean()
    dtmi3 = df['Tmin'].ix[92598:138896].mean()
    dr4 = df['Rain'].ix[138897: 185195].mean()
    dtma4 = df['Tmax'].ix[138897: 185195].mean()
    dtmi4 = df['Tmin'].ix[138897: 185195].mean()
    dr5 = df['Rain'].ix[185196:231495].mean()
    dtma5 = df['Tmax'].ix[185196:231495].mean()
    dtmi5 = df['Tmin'].ix[185196:231495].mean()
    dr1 = str(dr1)
    dtma1 = str(dtma1)
    dtmi1 = str(dtmi1)
    dr2 = str(dr2)
    dtma2 = str(dtma2)
    dtmi2 = str(dtmi2)
    dr3 = str(dr3)
    dtma3 = str(dtma3)
    dtmi3 = str(dtmi3)
    dr4 = str(dr4)
    dtma4 = str(dtma4)
    dtmi4 = str(dtmi4)
    dr5 = str(dr5)
    dtma5 = str(dtma5)
    dtmi5 = str(dtmi5)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/Promedios.csv","a")
    archivo.write("PROMEDIOS DE LOS 5 DÍAS\n ")
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr1, dtma1, dtmi1))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr2, dtma2, dtmi2))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr3, dtma3, dtmi3))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr4, dtma4, dtmi4))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n ".format(dr5, dtma5, dtmi5))



def calcularUnidadesCalorBase10():
    """
    Función que permite el calculo de unidades Calor
    param: tmax: Temperatura Máxima
    param: tmin: Temperatura Mínima
    param: tbase: Temperatura Base = 10
    Formula uc = tmax + tmin / 2 - tbase
    Donde:
    uc =  unidades calor
    tmax = temperatura máxima
    tmin = tempratura mínima
    tbase = 10
    si tmax > 30 :  tmax = 30
    si tmin < 10 : tmin = 10
    si uc < 0 : uc = 0
    """


    arryTmax = []
    arryTmin = []

    for x in df["Tmax"]:
        arryTmax.append(x)

    for y in df["Tmin"]:
        arryTmin.append(y)

    len(df)
    arreglo = []

    for d in range(len(df)):
        if arryTmax[d] > 30:
            arryTmax[d] = 30
        if arryTmin[d] < 10:
            arryTmin[d] = 10
        uc =  (arryTmax[d] + arryTmin[d]) / 2 - 10
        #arreglo.append(uc)
        if uc <= 0:
            arreglo.append(0)
        else:
            arreglo.append(uc)
    arreglo
    df["UC"]= np.array(arreglo)

    x = pd.DataFrame.to_csv(df)
    archivo = open ("/home/caro/Documentos/becarios_utna/ejercicios/Resultados/UC.csv","a")
    archivo.write(x)

#dia1_crear()
#dia2_crear()
#dia3_crear()
#dia4_crear()
#dia5_crear()
#latlong_crear()
#Promedios_crear()
#PromediosLatLong_crear()
#UC_crear()
#latlong_escribir()
#dia1_escribir()
#dia2_escribir()
#dia3_escribir()
#dia4_escribir()
#dia5_escribir()
#Promedios_escribir()
#PromediosLatLong_escribir()
#calcularUnidadesCalorBase10()
