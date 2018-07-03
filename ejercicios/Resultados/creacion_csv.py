#######################################
# Author: Lucrecia Rodríguez
# Email: lucrepbarone@gmail.com
# Date: 2018-06-28
# Version: 1.0
#######################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
plt.style.use("ggplot")
df = pd.read_csv("/home/acer/Documentos/examen_final.csv")
df1=df.ix[0:46298] #1er dia
df2=df.ix[46299:92597] #2 do dia
df3=df.ix[92598:138896]  #3 er dia
df4=df.ix[138897:185195]  #4 to dia
df5=df.ix[185196:231495]  #5 to dia
dfcorte=df[(df['Lat']>21.0) & (df['Lat'] <24.0) & (df['Long']>-104.0) & (df['Long']<-100.0 )]



#print(df)
#Creacion de los archivos csv por dia
"""
def crear_archivo1():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia1.csv","w")
    archivo.close()
def crear_archivo2():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia2.csv","w")
    archivo.close()
def crear_archivo3():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia3.csv","w")
    archivo.close()
def crear_archivo4():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia4.csv","w")
    archivo.close()
def crear_archivo5():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia5.csv","w")
    archivo.close()
def crear_archivoCorte():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/corte.csv","w")
    archivo.close()
def crear_archivoMedias():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/medias.csv","w")
    archivo.close()
def crear_archivoMediasCorte():
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/mediasCorte.csv","w")
    archivo.close()
"""
#escribir
def write1():
    x=pd.DataFrame.to_csv(df1)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia1.csv","a")
    archivo.write(x)
def write2():
    x=pd.DataFrame.to_csv(df2)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia2.csv","a")
    archivo.write(x)
def write3():
    x=pd.DataFrame.to_csv(df3)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia3.csv","a")
    archivo.write(x)
def write4():
    x=pd.DataFrame.to_csv(df4)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia4.csv","a")
    archivo.write(x)
def write5():
    x=pd.DataFrame.to_csv(df5)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/dia5.csv","a")
    archivo.write(x)
def writeCorte():
    x=pd.DataFrame.to_csv(dfcorte)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/corte.csv","a")
    archivo.write(x)
def writeMedia():
    #DIA 1
    dr1=df["Rain"].ix[0:46298].mean()
    dtx1=df["Tmax"].ix[0:46298].mean()
    dtn1=df["Tmin"].ix[0:46298].mean()
    #DIA 2
    dr2=df["Rain"].ix[46299:92597].mean()
    dtx2=df["Tmax"].ix[46299:92597].mean()
    dtn2=df["Tmin"].ix[46299:92597].mean()
    #DIA 3
    dr3=df["Rain"].ix[92598:138896].mean()
    dtx3=df["Tmax"].ix[92598:138896].mean()
    dtn3=df["Tmin"].ix[92598:138896].mean()
    #DIA 4
    dr4=df["Rain"].ix[138897:185195].mean()
    dtx4=df["Tmax"].ix[138897:185195].mean()
    dtn4=df["Tmin"].ix[138897:185195].mean()
    #DIA 5
    dr5=df["Rain"].ix[185196:231495].mean()
    dtx5=df["Tmax"].ix[185196:231495].mean()
    dtn5=df["Tmin"].ix[185196:231495].mean()
    #print(dr1)
    #x=pd.DataFrame.to_csv(dr1)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/medias.csv","a")
    dr1=str(dr1)
    dr2=str(dr2)
    dr3=str(dr3)
    dr4=str(dr4)
    dr5=str(dr5)
    dtx1=str(dtx1)
    dtx2=str(dtx2)
    dtx3=str(dtx3)
    dtx4=str(dtx4)
    dtx5=str(dtx5)
    dtn1=str(dtn1)
    dtn2=str(dtn2)
    dtn3=str(dtn3)
    dtn4=str(dtn4)
    dtn5=str(dtn5)
    archivo.write("Medias \n")
    archivo.write("Dia 1 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr1,dtx1,dtn1))
    archivo.write("\nDia 2 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr2,dtx2,dtn2))
    archivo.write("\nDia 3 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr3,dtx3,dtn3))
    archivo.write("\nDia 4 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr4,dtx4,dtn4))
    archivo.write("\nDia 5 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr5,dtx5,dtn5))


def writeMediaCorte():
    a=df[(df['Lat']>21.0) & (df['Lat'] <24.0) & (df['Long']>-104.0) & (df['Long']<-100.0 )]
    #DIA 1
    dr1=a["Rain"].ix[0:46298].mean()
    dtx1=a["Tmax"].ix[0:46298].mean()
    dtn1=a["Tmin"].ix[0:46298].mean()
    #DIA 2
    dr2=a["Rain"].ix[46299:92597].mean()
    dtx2=a["Tmax"].ix[46299:92597].mean()
    dtn2=a["Tmin"].ix[46299:92597].mean()
    #DIA 3
    dr3=a["Rain"].ix[92598:138896].mean()
    dtx3=a["Tmax"].ix[92598:138896].mean()
    dtn3=a["Tmin"].ix[92598:138896].mean()
    #DIA 4
    dr4=a["Rain"].ix[138897:185195].mean()
    dtx4=a["Tmax"].ix[138897:185195].mean()
    dtn4=a["Tmin"].ix[138897:185195].mean()
    #DIA 5
    dr5=a["Rain"].ix[185196:231495].mean()
    dtx5=a["Tmax"].ix[185196:231495].mean()
    dtn5=a["Tmin"].ix[185196:231495].mean()
    #print(dr1)
    #x=pd.DataFrame.to_csv(dr1)
    archivo=open("/home/acer/Documentos/becarios_utna/ejercicios/Resultados/mediasCorte.csv","a")
    dr1=str(dr1)
    dr2=str(dr2)
    dr3=str(dr3)
    dr4=str(dr4)
    dr5=str(dr5)
    dtx1=str(dtx1)
    dtx2=str(dtx2)
    dtx3=str(dtx3)
    dtx4=str(dtx4)
    dtx5=str(dtx5)
    dtn1=str(dtn1)
    dtn2=str(dtn2)
    dtn3=str(dtn3)
    dtn4=str(dtn4)
    dtn5=str(dtn5)
    archivo.write("Medias a partir del corte con Lat y Long\n")
    archivo.write("Dia 1 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr1,dtx1,dtn1))
    archivo.write("\nDia 2 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr2,dtx2,dtn2))
    archivo.write("\nDia 3 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr3,dtx3,dtn3))
    archivo.write("\nDia 4 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr4,dtx4,dtn4))
    archivo.write("\nDia 5 \n")
    archivo.write("Media de Rain: {}  \nMedia de Tmax: {} \nMedia de Tmin: {}".format(dr5,dtx5,dtn5))


def unidadCalor():
    arrayTmax=[]
    arrayTmin=[]
    for e in df["Tmax"]:
        arrayTmax.append(e)
        #print(e)
    for e in df["Tmin"]:
        arrayTmin.append(e)
    #arrayTmax
    #arrayTmin
    #uc=tmax+tmin/2-10
    len(df)
    array=[]
    #arrayTmax[0]
    for i in range(len(df)):
        uc=(arrayTmax[i]+arrayTmin[i])/2-10
        if uc<=0:
            array.append(0)
        else:
            array.append(uc)
    array
    df["UC"]=np.array(array)
    print(df)
"""
print(" \033[4;35;47m"+"Opcion 1"+"\033[0;m")
print("Del archivo examen_final.csv genera un archivo csv para cada día, estos csv deben de guardarse en la carpeta de resultados")
print(" \033[4;35;47m"+"Opcion 2"+"\033[0;m")
print("De la información que se tiene, genera un corte de información para las columnas Lat y Long con los siguientes valores \n Lat > 21.0 \n Lat < 24.0 \n Long > -104.0\nLong < -100.0")
print(" \033[4;35;47m"+"Opcion 3"+"\033[0;m")
print("Calcula las medias de cada una de las variables Rain, Tmax, Tmin por día y guardalas en un csv en la carpeta de resultados")
print(" \033[4;35;47m"+"Opcion 4"+"\033[0;m")
print("Calcula las medias de cada una de las variables Rain, Tmax, Tmin por día del corte de información limitado por las columnas Lat y Long con los siguientes\n Lat > 21.0 \n Lat < 24.0 \n Long > -104.0\nLong < -100.0\ny guardalas en un csv en la carpeta de resultados")
print(" \033[4;35;47m"+"Opcion 5"+"\033[0;m")
print("Calcular las Unidades Calor (UC) para cada una de las filas con la formúla que se indica en el programa.")
opcion=int(input("Elige una opcion: "))
if opcion==1:
    crear_archivo1()
    crear_archivo2()
    crear_archivo3()
    crear_archivo4()
    crear_archivo5()
    write1()
    write2()
    write3()
    write4()
    write5()
    print("5 Archivos creados revisa la carpeta Resultados")
elif opcion==2:
    crear_archivoCorte()
    writeCorte()
    print("Archivo creado revisa la carpeta Resultados")
elif opcion==3:
    crear_archivoMedias()
    writeMedia()
    print("Archivo creado revisa la carpeta Resultados")
elif opcion==4:
    crear_archivoMediasCorte()
    writeMediaCorte()
    print("Archivo creado revisa la carpeta Resultados")
elif opcion==5:
    unidadCalor()
else:
    print("Las opciones son del 1 al 5")
"""
crear_archivo1()
crear_archivo2()
crear_archivo3()
crear_archivo4()
crear_archivo5()
write1()
write2()
write3()
write4()
write5()
crear_archivoCorte()
writeCorte()
crear_archivoMedias()
writeMedia()
crear_archivoMediasCorte()
writeMediaCorte()
unidadCalor()
print("Archivos creado revisa la carpeta Resultados")
