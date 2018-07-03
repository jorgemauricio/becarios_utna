

def cadenna():
    cad="A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 @ # $ + - & / *"
    cad= cad.split()
    cadena=len(cad)
    return cad, cadena

def ciclo(x,y):
    cad, cadena= cadenna()
    let=""
    letra_encriptada=""
    cont=0
    cont2=0
    for i in cad:
        if i == x:
            cont2= cont
            let=i
            if cont >= cadena -y:
                resultado = cadena-cont-1
                res= y- resultado
                print (res,cont)
                letra_encriptada= cad[res-1]
            else:
                cont2= cont2 + y
                letra_encriptada= cad[cont2]
        cont =  cont + 1
    return let, letra_encriptada

def codificar ():
    arr1=[]
    arr2=[]
    num= int(input("Ingresa el numero de codificacion: "))
    div= num//72
    res= num%72
    print (res)
    archivo= open("mensaje.txt", "r")
    for linea in archivo.readlines():
        print(linea)
        for letra in linea:
            if letra==" ":
                arr1.append(" ")
                arr2.append(" ")
            else:
                if div>=1:
                    a1, a2= ciclo(letra,res)
                    arr1.append(a1)
                    arr2.append(a2)
                else:
                    a1, a2= ciclo(letra, num)
                    arr1.append(a1)
                    arr2.append(a2)
    arr2="".join(arr2)
    arr1="".join(arr1)
    print("Decodificado:", arr2)
    print("Codificado:", arr1)


def decodificar ():
    arr1=[]
    arr2=[]
    num= int(input("Ingresa el numero de codificacion: "))
    div= num%72
    res= num*72
    print (res)
    archivo= open("mensaje.txt", "r")
    for linea in archivo.readlines():
        print(linea)
        for letra in linea:
            if letra==" ":
                arr1.append(" ")
                arr2.append(" ")
            else:
                if div>=1:
                    a1,a2= ciclo(letra, res)
                    arr1.append(a1)
                    arr2.append(a2)
                else:
                    a1, a2= ciclo(letra, num)
                    arr1.append(a1)
                    arr2.append(a2)
    arr2="".join(arr2)
    arr1="".join(arr1)
    print("Decodificado:", arr2)
    print("Codificado:", arr1)

codificar ()

"""
def sin(txt):
		nuevo=""
		for x in txt:
	    		if x=='|':
 	      			nuevo = nuevo+' '
 	    		else:
        			nuevo = nuevo+x
   		return nuevo

def espacio(mens):
		espacios= ""
		for x in texto:
	    		if x==' ':
 	      			espacios = espacios+'|'
 	    		else:
        			espacios = espacios+x.lower()
   		return espacios






for palabra in mens:
    for letra in palabra:
        print (letra)
#print(mens)
"""
"""
def abriarch():
archivo = open ('mensaje.txt','w')
archivo.close()
"""
