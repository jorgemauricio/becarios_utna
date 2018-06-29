
def crear_archivo():
    archivo=open("mensaje.txt","w")
    archivo.close()
#crear_archivo()

#crip=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def cadena():
    crip="A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 * / # $ % & + -"
    crip=crip.split()
    longitud=len(crip)
    #print("#### ",longitud)
    return crip,longitud
#print(crip[0])

#x="e"
def ciclo(x,n):
    crip,longitud=cadena()
    let=""
    letra_encrip=""
    cont=0
    c=0
    for i in crip:
        if i==x:
            c=cont
            let=i
            if cont>=longitud-n:
                res=longitud-cont-1
                r=n-res
                print(r,cont)
                letra_encrip=crip[r-1]
            else:
                c=c+n
                letra_encrip=crip[c]
        cont=cont+1
    return let,letra_encrip

def codificar():
    arr=[]
    arr2=[]
    num=int(input("Ingresa el número de codificación:  "))
    div=num//72
    res=num%72
    print(res)
    archivo=open("mensaje.txt","r")
    for linea in archivo.readlines():
        print(linea)
        for letra in linea:
            if letra==" ":
                arr.append(" ")
                arr2.append(" ")
            else:
                if div>=1:
                    a1,a2=ciclo(letra,res)
                    arr.append(a1)
                    arr2.append(a2)
                else:
                    a1,a2=ciclo(letra,num)
                    arr.append(a1)
                    arr2.append(a2)

    arr2="".join(arr2)
    arr="".join(arr)
    print("Decodificado: ",arr2)
    print("Codificado:   ",arr)
    archivo.close()



def ciclodec(x,n):
    crip,longitud=cadena()
    let=""
    letra_encrip=""
    cont=0
    c=0
    for i in crip:
        if i==x:
            let=i
            if cont>=longitud:
                res=longitud+cont-1
                r=n+res
                letra_encrip=crip[r-1]
            else:
                c=cont
                letra_encrip=crip[cont-n]
        cont=cont+1
    return let,letra_encrip

def decodificar():
    arr=[]
    arr2=[]
    num=int(input("Ingresa el número de codificación:  "))
    div=num//72
    res=num%72
    print(res)
    archivo=open("mensaje.txt","r")
    for linea in archivo.readlines():
        #print(linea)
        #acum=0
        for letra in linea:
            #print("####### ",letra)
            if letra==" ":
                arr.append(" ")
                arr2.append(" ")
            else:
                if div>=1:
                    a1,a2=ciclodec(letra,res)
                    arr.append(a1)
                    arr2.append(a2)
                else:
                    a1,a2=ciclodec(letra,num)
                    arr.append(a1)
                    arr2.append(a2)
            #acum=acum+1
        #print(acum-1)

    arr2="".join(arr2)
    arr="".join(arr)
    print("Decodificado: ",arr2)
    print("Codificado:   ",arr)
    archivo.close()
print("1. Codificar")
print("2. Decodificar")
opc=int(input("Elige una opción:  "))
if opc==1:
    codificar()
elif opc==2:
    decodificar()
else:
    print("elige un número 1 ó 2")
