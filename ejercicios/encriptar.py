
# Author: Carolina Briano
# Email: carolinabriano15@gmail.com
# Date: 2018-07-02
def cadena():
    enc = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 # @ % &"
    enc = enc.split()
    cad = len(enc)
    return enc, cad

def ciclo(x, y):
    enc, cad = cadena()
    car = ""
    car_enc=""
    con1 = 0
    con2 = 0
    for i in enc:
        if i == x:
            con2 = con1
            car = i
            if con1 >= cad - y:
                res = cad - con1 - 1
                r = y - res
                print(r,con1)
                car_enc = enc[r-1]
            else:
                con2 = con2 + y
                car_enc = enc[con2]
        con1 =  con1 + 1
    return car, car_enc


def codificar():
    arr1 = []
    arr2 = []
    num = int(input("Ingresar el número a codificar: "))
    div = num // 72
    res = num % 72
    print(res)
    archivo = open("mensaje.txt", "r")
    for linea in archivo.readlines():
        print(linea)
        for letra in linea:
            if letra == " ":
                arr1.append(" ")
                arr2.append(" ")
            else:
                if div >= 1:
                    c1, c2 = ciclo(letra, res)
                    print("##### letra  ",c1)
                    print("##### res  ",c2)
                    arr1.append(c1)
                    arr2.append(c2)
                else:
                    c1, c2 = ciclo(letra, num)
                    arr1.append(c1)
                    arr2.append(c2)
    arr1 = "".join(arr1)
    arr2 = "".join(arr2)
    print("Decodifición: ", arr2)
    print("Codificación: ", arr1)


def decodificar():
    arr1 = []
    arr2 = []
    num = int(input("Ingresar el número a decodificar: "))
    div = num // 72
    res = num % 72
    print(res)
    archivo = open("mensaje.txt", "r")
    for linea in archivo.readlines():
        print(linea)
        for letra in linea:
            if letra == " ":
                arr1.append(" ")
                arr2.append(" ")
            else:
                if div >= 1:
                    c1, c2 = ciclo(letra, res)
                    print("##### letra  ",c1)
                    print("##### res  ",c2)
                    arr1.append(c1)
                    arr2.append(c2)
                else:
                    c1, c2 = ciclo(letra, num)
                    arr1.append(c1)
                    arr2.append(c2)
    arr1 = "".join(arr1)
    arr2 = "".join(arr2)
    print("Decodifición: ", arr2)
    print("Codificación: ", arr1)

#codificar()
decodificar()

"""
def espacio(mensaje):
    espacios= ""
    for x in mensaje:
        if x == ' ':
            espacios = espacios + '|'
        else:
            espacios = espacios + x.lower()
    return espacios


archivo = open("mensaje.txt", "r")
#archivo.read()
mensaje = archivo.read()
print(mensaje)
me = (len(mensaje))
encrip=int(input("Numero a encriptar: "))

posicion= 0
en=encrip[0]
index = enc.index(en)
encadena= ""
suma = 0
espacios=""
espacios=espacio(mensaje)

for x in espacios:
    for n in range(menlen):
        con = 0
        if x == enc[n]:
            con = n + index
            if con <= enc:
                encadena = encadena + enc[con]
            else:
                suma = restar(enc, con)
                encadena = encadena+ enc [suma]
                suma = 0
print ("mensaje: {}".format(encadena))
print ("Clave es: {}".format(enc))"""
