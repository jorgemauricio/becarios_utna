"""
Generar un programa que pregunte al usuario
que área es la que desea calcular

1. triángulo
2. circulo
3. cuadrado
4. rectangulo
5. salir
"""

def area_triangulo(b,h):
    """
    Función que calcula el área de un triángulo
    param: b: base
    param: h: altura
    return: área del triángulo
    """
    return (b * h) / 2

def area_circulo(r):
    """
    Función que calcula el área de un circulo
    param: r: radio
    return area del circulo
    """
    return (3.1416 * r)**2

def area_cuadrado(l):
    """
    Función que calcula el área de un cuadrado
    param: l: lado
    return area del cuadrado
    """
    return (l*l)
def area_rectangulo(b, h):
    """
    Función que calcula el área de un rectangulo
    param: b: base
    param: h: altura
    return area del rectangulo
    """
    return (b*h)


while True:
    print("\n")
    print("Programa para calcular las áreas de figuras")
    print("1: Triángulo \n")
    print("2: Circulo \n")
    print("3: Cuadrado \n")
    print("4: Rectangulo \n")
    print("5: Salir \n")
    opcion = input("Ingrese la opción deseada: ")

    if opcion=='5':
        print("Cerrando..")
        break
    elif opcion=='1':
        b = float(input("Ingresa la base: "))
        h = float(input("Ingresa la altura: "))
        print(area_triangulo(b,h))
    elif opcion=='2':
        r = float(input("Ingrese el radio: "))
        print(area_circulo(r))
    elif opcion=='3':
        l = float(input("Ingrese el lado: "))
        print(area_cuadrado(l))
    elif opcion=='4':
        b = float(input("Ingresa la base: "))
        h = float(input("Ingresa la altura: "))
        print(area_rectangulo(b,h))
    else:
        print("Ingrese una opción correcta")
