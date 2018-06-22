#from funciones  import area_cuadrado

def area_triangulo(b,h):
    """
    Función que calcula el área de un triángulo
    param: b: base
    param: h: altura
    return: área del triángulo
    """
    return (b * h) / 2

while True:
    print("Programa para calcular el área de un triángulo")
    b = int(input("Ingresa la base: "))
    h = int(input("Ingresa la altura: "))
    print(area_triangulo(b,h))
