#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jaqueline Espinoza
# Email: jaqueespinoza791@gmail.com
# Date: 2018-02-01
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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
plt.style.use("ggplot")
# función main()


# leer csv
df=pd.read_csv("/home/jackie/Documentos/examen_final.csv")
df1=df.ix[0:46298]#primer día
df2=df.ix[46299:92597]#segundo día
df3=df.ix[92598:138896]#tercer día
df4=df.ix[138897:185195]#cuarto día
df5=df.ix[185196:231495]#quinto día
b=df[(df['Lat']>21.0) & (df['Lat']<24.0) & (df['Long']> -104.0) & (df['Long']< -100.0)]#Latitud y Longitud


#print(df)

# generar mis csv por día
def creardia1():
    archivo=open('Dia1.csv','w')
    archivo.close()
def creardia2():
    archivo=open('Dia2.csv','w')
    archivo.close()
def creardia3():
    archivo=open('Dia3.csv','w')
    archivo.close()
def creardia4():
    archivo=open('Dia4.csv','w')
    archivo.close()
def creardia5():
    archivo=open('Dia5.csv','w')
    archivo.close()


def crearLatLong():
    archivo=open('LatLong.csv','w')
    archivo.close()
#calcular la media de tmin, tmax, rain
#def mediaPorDias():
    #archivo=open('MediaPorDias.csv','w')
    #archivo.close()

def mediaLatiLong():
    archivo=open('MediaLatiLong4.csv','w')
    archivo.close()


def writedia1():
    x=pd.DataFrame.to_csv(df1)
    archivo=open("Dia1.csv","a")
    archivo.write(x)
def writedia2():
    x=pd.DataFrame.to_csv(df2)
    archivo=open("Dia2.csv","a")
    archivo.write(x)
def writedia3():
    x=pd.DataFrame.to_csv(df3)
    archivo=open("Dia3.csv","a")
    archivo.write(x)
def writedia4():
    x=pd.DataFrame.to_csv(df4)
    archivo=open("Dia4.csv","a")
    archivo.write(x)
def writedia5():
    x=pd.DataFrame.to_csv(df5)
    archivo=open("Dia5.csv","a")
    archivo.write(x)

def writeLatLong():
    x=pd.DataFrame.to_csv(b)
    archivo=open("LatLong.csv","a")
    archivo.write(x)

def mediasDias():
    dr1= b['Rain'].ix[0:46298].mean()
    dtm1= b['Tmax'].ix[0:46298].mean()
    dtmin1= b['Tmin'].ix[0:46298].mean()
    dr2= b['Rain'].ix[46299:92597].mean()
    dtm2= b['Tmax'].ix[46299:92597].mean()
    dtmin2= b['Tmin'].ix[46299:92597].mean()
    dr3= b['Rain'].ix[92598:138896].mean()
    dtm3= b['Tmax'].ix[92598:138896].mean()
    dtmin3= b['Tmin'].ix[92598:138896].mean()
    dr4= b['Rain'].ix[138897:185195].mean()
    dtm4= b['Tmax'].ix[138897:185195].mean()
    dtmin4= b['Tmin'].ix[138897:185195].mean()
    dr5= b['Rain'].ix[185196:231495].mean()
    dtm5= b['Tmax'].ix[185196:231495].mean()
    dtmin5= b['Tmin'].ix[185196:231495].mean()

    dr1=str(dr1)
    dtm1=str(dtm1)
    dtmin1=str(dtmin1)
    dr2=str(dr2)
    dtm2=str(dtm2)
    dtmin2=str(dtmin2)
    dr3=str(dr3)
    dtm3=str(dtm3)
    dtmin3=str(dtmin3)
    dr4=str(dr4)
    dtm4=str(dtm4)
    dtmin4=str(dtmin4)
    dr5=str(dr5)
    dtm5=str(dtm5)
    dtmin5=str(dtmin5)
    archivo=open("MediaLatiLong4.csv","a")
    archivo.write("PROMEDIOS DE LOS 5 DÍAS CON CORTE DE LATITUD Y LONGITUD\n")
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr1,dtm1,dtmin1))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr2,dtm2,dtmin2))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr3,dtm3,dtmin3))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr4,dtm4,dtmin4))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr5,dtm5,dtmin5))



def mediasPorDia():
    dr1= df['Rain'].ix[0:46298].mean()
    dtm1= df['Tmax'].ix[0:46298].mean()
    dtmin1= df['Tmin'].ix[0:46298].mean()
    dr2= df['Rain'].ix[46299:92597].mean()
    dtm2= df['Tmax'].ix[46299:92597].mean()
    dtmin2= df['Tmin'].ix[46299:92597].mean()
    dr3= df['Rain'].ix[92598:138896].mean()
    dtm3= df['Tmax'].ix[92598:138896].mean()
    dtmin3= df['Tmin'].ix[92598:138896].mean()
    dr4= df['Rain'].ix[138897:185195].mean()
    dtm4= df['Tmax'].ix[138897:185195].mean()
    dtmin4= df['Tmin'].ix[138897:185195].mean()
    dr5= df['Rain'].ix[185196:231495].mean()
    dtm5= df['Tmax'].ix[185196:231495].mean()
    dtmin5= df['Tmin'].ix[185196:231495].mean()

    dr1=str(dr1)
    dtm1=str(dtm1)
    dtmin1=str(dtmin1)
    dr2=str(dr2)
    dtm2=str(dtm2)
    dtmin2=str(dtmin2)
    dr3=str(dr3)
    dtm3=str(dtm3)
    dtmin3=str(dtmin3)
    dr4=str(dr4)
    dtm4=str(dtm4)
    dtmin4=str(dtmin4)
    dr5=str(dr5)
    dtm5=str(dtm5)
    dtmin5=str(dtmin5)
    archivo=open("MediaPorDias.csv","a")
    archivo.write("PROMEDIOS DE LOS 5 DÍAS\n")
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr1,dtm1,dtmin1))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr2,dtm2,dtmin2))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr3,dtm3,dtmin3))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr4,dtm4,dtmin4))
    archivo.write("Rain {}, Tmax {}, Tmin {}\n".format(dr5,dtm5,dtmin5))


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
    arrayTmax=[]
    arrayTmin=[]
    for x in df["Tmax"]:
        arrayTmax.append(x)
    for y in df["Tmin"]:
        arrayTmin.append(y)

    len(df)
    arreglo=[]

    for d in range(len(df)):
        if arrayTmax[d] > 30:
            arrayTmax[d] = 30
        if arrayTmin[d] < 10:
            arrayTmin[d] = 10
        uc= (arrayTmax[d] + arrayTmin[d]) / 2 - 10
        #arreglo.append(uc)
        if uc<=0:
            arreglo.append(0)
        else:
            arreglo.append(uc)
    #arreglo
    df["UC"]=np.array(arreglo)
    print(df)
    x=pd.DataFrame.to_csv(df)
    archivo=open("UC.csv","a")
    archivo.write(x)















"""
creardia1()
writedia1()
creardia2()
writedia2()
creardia3()
writedia3()
creardia4()
writedia4()
creardia5()
writedia5()
crearLatLong()
writeLatLong()
mediaPorDias()
mediasPorDia()
#mediaLatiLong()
mediasDias()"""
calcularUnidadesCalorBase10()
#if __name__ == '__main__':
#    main()
