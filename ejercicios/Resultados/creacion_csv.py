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
