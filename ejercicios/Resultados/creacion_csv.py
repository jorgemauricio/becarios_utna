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



print(df)
#Creacion de los archivos csv por dia
def crear_archivo1():
    archivo=open("dia1.csv","w")
    archivo.close()
def crear_archivo2():
    archivo=open("dia2.csv","w")
    archivo.close()
def crear_archivo3():
    archivo=open("dia3.csv","w")
    archivo.close()
def crear_archivo4():
    archivo=open("dia4.csv","w")
    archivo.close()
def crear_archivo5():
    archivo=open("dia5.csv","w")
    archivo.close()
def crear_archivoCorte():
    archivo=open("corte.csv","w")
    archivo.close()
def crear_archivoMedias():
    archivo=open("medias.csv","w")
    archivo.close()
def crear_archivoMediasCorte():
    archivo=open("mediasCorte.csv","w")
    archivo.close()
#escribir
def write1():
    x=pd.DataFrame.to_csv(df1)
    archivo=open("dia1.csv","a")
    archivo.write(x)
def write2():
    x=pd.DataFrame.to_csv(df2)
    archivo=open("dia2.csv","a")
    archivo.write(x)
def write3():
    x=pd.DataFrame.to_csv(df3)
    archivo=open("dia3.csv","a")
    archivo.write(x)
def write4():
    x=pd.DataFrame.to_csv(df4)
    archivo=open("dia4.csv","a")
    archivo.write(x)
def write5():
    x=pd.DataFrame.to_csv(df5)
    archivo=open("dia5.csv","a")
    archivo.write(x)
def writeCorte():
    x=pd.DataFrame.to_csv(dfcorte)
    archivo=open("corteMedia.csv","a")
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
    print(dr1)
    #x=pd.DataFrame.to_csv(dr1)
    archivo=open("medias.csv","a")
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
    print(dr1)
    #x=pd.DataFrame.to_csv(dr1)
    archivo=open("mediasCorte.csv","a")
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
crear_archivo1()
#crear_archivo2()
#crear_archivo3()
#crear_archivo4()
#crear_archivo5()
#crear_archivoCorte()
#crear_archivoMedias()
#crear_archivoMediasCorte()
write1()
#write2()
#write3()
#write4()
#write5()
#writeCorte()
#writeMedia()
#writeMediaCorte()
