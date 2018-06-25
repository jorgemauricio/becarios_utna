
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
# No. Examen 5
# Valor: 10 puntos
# Corregir el siguiente código en c
#FUNCIONA


#include <stdio.h>
def main():

    # Print Menu
    print("El siguiente programa te solicitara que ingreses dos números")
    print("Posteriormente te indicara los números que te solicito")
    print("Primero desplegando el primer número")
    print("Y en seguida el segundo número")

    # printf() dislpays the formatted output
    number1=input("Ingresa el primer entero: ")

    # scanf() reads the formatted input and stores them
    #scanf("%c", number1)

    # printf() dislpays the formatted output
    Number3=input("Ingresa el segundo entero: ")

    #scanf() reads the formatted input and stores them
    #scanf("%s", Number3)

    # printf() displays the formatted output
    print("Primer número: ", number1)
    print("Segundo número: ", Number3)

    #return 1


if __name__=='__main__':
    main()
